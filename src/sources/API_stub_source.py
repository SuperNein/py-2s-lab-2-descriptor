from typing import List, Optional, Iterable, Dict

from src.models import Task
from src.common.constants import API_STUB_TASKS


class APIStubTasksSource:
    def __init__(self, url: str):
        self._url = url
        self._data: Optional[List[Dict]] = None

    def _request(self) -> None:
        self._data = [
            {"id": i, "payload": {"data": f"task_{i}"}}
            for i in range(API_STUB_TASKS)
        ]

    def get_tasks(self) -> Iterable[Task]:
        if self._data is None:
            self._request()

        return [
            Task(task_id=task["id"], payload=task["payload"])
            for task in self._data
        ]
