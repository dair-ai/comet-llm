import collections

from typing import Dict


class LogsRegistry:
    def __init__(self) -> None:
        self._registry = collections.defaultdict(lambda: 0)

    def register_log(self, project_url: str) -> None:
        self._registry[project_url] += 1
    
    def summary(self) -> Dict[str, int]:
        return self._registry.copy()