import pytest

from src.core.enums import TaskStatus
from src.core.models import Task


@pytest.mark.parametrize(
    "status, is_closed",
    [
        (TaskStatus.new, False),
        (TaskStatus.in_progress, False),
        (TaskStatus.done, True),
        (TaskStatus.cancelled, True)
    ]
)
def test_generator_source(status, is_closed):
    task = Task(payload="")
    task.status = status

    assert task.is_closed == is_closed
