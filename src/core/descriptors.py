import uuid
from typing import Optional, Any

from src.core.enums import TaskPriority, TaskStatus
from src.core.exceptions import InvalidPriorityError, InvalidStatusError


class BaseDescriptor:
    def __set_name__(self, owner: type, name: str) -> None:
        self.public_name = name
        self.private_name = f"_{name}"

    def __get__(self, instance: Optional[object], owner: type) -> Any:
        if instance is None:
            return self
        return getattr(instance, self.private_name)


class TaskIdDescriptor(BaseDescriptor):
    def __get__(self, instance: Optional[object], owner: type) -> Any:
        if instance is None:
            return self

        if not hasattr(instance, self.private_name):
            setattr(instance, self.private_name, uuid.uuid4())

        return getattr(instance, self.private_name)

    def __set__(self, instance: object, value: Any) -> None:
        raise AttributeError(f"Attribute '{self.public_name}' is read-only")


class CreatedAtDescriptor(BaseDescriptor):
    def __get__(self, instance: Optional[object], owner: type) -> Any:
        if instance is None:
            return self

        return getattr(instance, self.private_name).strftime("%Y-%m-%d %H:%M:%S")


class PriorityDescriptor(BaseDescriptor):
    PRIORITIES = {p for p in TaskPriority}

    def __set__(self, instance: object, value: Any) -> None:
        if isinstance(value, TaskPriority):
            validated_value = value.value

        elif isinstance(value, int) and value in TaskPriority:
            validated_value = value
        else:
            raise InvalidPriorityError(
                f"Priority must be one of {self.PRIORITIES}, got {value}"
            )

        setattr(instance, self.private_name, validated_value)


class StatusDescriptor(BaseDescriptor):
    STATUSES = {s for s in TaskStatus}

    def __set__(self, instance: object, value: Any) -> None:
        if isinstance(value, TaskStatus):
            validated_value = value.value

        elif isinstance(value, int) and value in TaskStatus:
            validated_value = value
        else:
            raise InvalidStatusError(
                f"Priority must be one of {self.STATUSES}, got {value}"
            )

        setattr(instance, self.private_name, validated_value)
