# Copyright IBM Corp. 2021. All Rights Reserved.

import re
from typing import Optional, Tuple, Set

from attr import attrs, evolve
import urllib.parse


_segment_regex: re.Pattern = re.compile(r'[a-zA-Z0-9:._+-]*')
_segment_allowed_characters: Set[str] = set(':._+-')

def _validate_segment(segment: str) -> None:
    if _segment_regex.fullmatch(segment):
        return

    forbidden_chars = set()
    for ch in segment:
        if ch in forbidden_chars:
            continue
        if not _segment_regex.fullmatch(ch):
            forbidden_chars.add(ch)

    forbidden_chars_str = ', '.join([f"'{ch}'" for ch in forbidden_chars])
    raise TypeError(f"segment '{segment}' contains forbidden characters: {forbidden_chars_str}")

@attrs(auto_attribs=True, frozen=True, kw_only=True)
class CpdScope:
    has_prefix: bool
    context: Optional[str]
    scope_type: str
    scope_id: str

    def __str__(self) -> str:
        result = f"{self.context or ''}/{self.scope_type}/{self.scope_id}"
        if self.has_prefix:
            result = "cpd://" + result
        return result

    @classmethod
    def try_from_string(cls, s: str) -> Tuple[Optional['CpdScope'], str]:
        s = s.strip()
        result = urllib.parse.urlparse(s)
        if result.scheme == 'cpd' or (result.scheme == '' and result.path.startswith('/')):
            return cls._from_parse_result(result)
        else:
            return None, s

    @classmethod
    def from_string(cls, s: str) -> 'CpdScope':
        result = urllib.parse.urlparse(s)
        return cls._from_parse_result(result)[0]

    @classmethod
    def _from_parse_result(cls, result: urllib.parse) -> Tuple['CpdScope', str]:
        has_prefix = False
        if result.scheme == 'cpd':
            has_prefix = True

        context = result.netloc
        if context == '':
            context = None

        query = result.query
        if query == '':
            query = None

        parts = result.path.split("/")
        if parts[0] == '':
            del parts[0]

        if len(parts) < 2:
            if len(parts) == 1 and parts[0].find("?") != -1:
                raise TypeError(f"CPD Scope for CPD Orchestration must use id, not query")
            raise TypeError(f"Wrong format of CPD Scope: '{result.geturl()}'")

        for part in parts:
            _validate_segment(part)

        scope_type = parts[0]
        scope_id = parts[1]
        other_parts = parts[2:]

        scope_types = [
            "projects",
            "spaces",
            "catalogs",
        ]

        if scope_type not in scope_types:
            raise TypeError(f"Unknown scope type: '{scope_type}'")

        remaining = "/".join(other_parts)
        if len(other_parts) > 0 and query is not None:
            remaining += '?' + query

        return CpdScope(
            has_prefix = has_prefix,
            context = context,
            scope_type = scope_type,
            scope_id = scope_id,
        ), remaining

@attrs(auto_attribs=True, frozen=True, kw_only=True)
class CpdPath:
    scope: Optional[CpdScope]
    path: str
    query: Optional[str] = None

    def __str__(self) -> str:
        result = []
        if self.scope is not None:
            result.append(str(self.scope))
        if self.path != '':
            result.append(self.path)
        result_str = "/".join(result)
        if self.query is not None:
            result_str += '?' + self.query
        return result_str

    @classmethod
    def from_string(cls, s: str) -> 'CpdPath':
        s = s.strip()
        scope, s = CpdScope.try_from_string(s)

        result = urllib.parse.urlparse(s)
        path = result.path
        parts = path.split("/")

        for part in parts:
            _validate_segment(part)

        query = result.query
        if query == '':
            query = None

        # if no scope, an additional case of "just by-id asset" must be checked
        if scope is None:
            if path.find("/") == -1: # no slashes --- it is by-id asset
                path = f"assets/{path}"

        if path.count("?") > 0:
            raise TypeError("Question mark can only be used once.")

        # what kind of path is it?
        if len(parts) > 3 and parts[0] == 'connections' and parts[2] == 'files':
            result = CpdPathToConnectionFile(scope=scope, path=path, query=query)
        else:
            result = CpdPath(scope=scope, path=path, query=query)
        return result

    def resource_id(self) -> Optional[str]:
        if self.query is not None:
            # if query is defined, cpd_path is not pointing at a specific
            # resource_id but instead, it searches using that query
            return None
        # otherwise, it's the last part of path
        return self.path.split('/')[-1]

    def is_relative(self) -> bool:
        return self.scope is None

    def resolve_at(self, cpd_scope: CpdScope) -> 'CpdPath':
        if self.scope is not None:
            return evolve(self)
        return evolve(self, scope=cpd_scope)

@attrs(auto_attribs=True, frozen=True, kw_only=True)
class CpdPathToConnectionFile(CpdPath):
    """CPD path pointing at a file inside some connection"""

    def resource_id(self) -> Optional[str]:
        return self.path.split('/')[1]

    def bucket_name(self) -> str:
        return self.path.split('/')[3]

    def file_path(self) -> str:
        return '/' + '/'.join(self.path.split('/')[4:])