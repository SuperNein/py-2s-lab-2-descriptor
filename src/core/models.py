from typing import Any


class Task:
    __slots__ = ("id", "payload")

    def __init__(self, task_id: int, payload: Any):
        self.id = task_id
        self.payload = payload
