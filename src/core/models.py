from typing import Any
from datetime import datetime

from src.core.enums import TaskPriority, TaskStatus
from src.core.descriptors import (
    TaskIdDescriptor,
    CreatedAtDescriptor,
    PriorityDescriptor,
    StatusDescriptor,
)


class Task:
    __slots__ = (
        "payload",
        "_id",
        "_priority",
        "_status",
        "_created_at",
    )

    id = TaskIdDescriptor()
    priority = PriorityDescriptor()
    status = StatusDescriptor()
    created_at = CreatedAtDescriptor()

    def __init__(
            self,
            payload: Any,
            priority: TaskPriority = TaskPriority.normal,
    ) -> None:
        self.payload = payload
        self._created_at = datetime.now()

        self.priority = priority
        self.status = TaskStatus.new


    @property
    def is_closed(self) -> bool:
        return self.status in {TaskStatus.done, TaskStatus.cancelled}
