import time

from src.core.models import Task
from src.core.enums import TaskStatus
from src.protocols.sources import TaskSource
from src.services.loader import TasksLoader


def process_tasks(source: TaskSource) -> list[Task]:
    """
    Processing tasks from source simulation.
    :return:    None
    """
    print(f"Start tasks from {source.__class__.__name__} processing...")
    loader = TasksLoader(source)
    tasks = loader.load()

    closed_tasks = []

    for task in tasks:
        task.status = TaskStatus.in_progress

        time.sleep(1)

        task.status = TaskStatus.done

        closed_tasks.append(task)
        print(f"Processed task {task.id}")

    print(f"Processed {len(closed_tasks)} tasks\n")

    return closed_tasks