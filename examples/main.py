from pathlib import Path

from src.protocols import TaskSource
from src.loader import TasksLoader
from src.sources.generator_source import GeneratorTaskSource
from src.sources.file_source import JSONTaskSource
from src.sources.API_stub_source import APIStubTasksSource


JSON_FILE_PATH = Path(__file__).parent / "tasks.json"


def process_tasks(source: TaskSource) -> None:
    """
    Processing tasks from source simulation.
    :return:    None
    """
    print(f"Start tasks from {source.__class__.__name__} processing...")
    loader = TasksLoader(source)
    tasks = loader.load()

    count = 0
    for task in tasks:
        count += 1

    print(f"Processed {count} tasks\n")


def main() -> None:
    """
    Main entry point for the application.
    :return:   None
    """
    sources = [
        GeneratorTaskSource(count=100),
        JSONTaskSource(JSON_FILE_PATH),
        APIStubTasksSource("https://url/tasks"),
    ]
    for source in sources:
        process_tasks(source)


if "__main__" == __name__:
    main()
