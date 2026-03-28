from typing import Iterable, Any

from src.core.models import Task


class GeneratorTaskSource:
    def __init__(self, count: int = 10, payload: Any = None):
        self._count = count
        self.payload = payload or {}

    def get_tasks(self) -> Iterable[Task]:
        for _ in range(self._count):
            yield Task(
                payload=self.payload,
            )
