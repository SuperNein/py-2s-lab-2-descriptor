from typing import Iterable

import pytest

from src.sources.generator_source import GeneratorTaskSource


@pytest.mark.parametrize(
    "count, payload",
    [
        (3, None),
        (2, [4, "2"]),
        (5, {4: "2"}),
        (1, 2)
    ]
)
def test_generator_source(count, payload):
    source = GeneratorTaskSource(count, payload)
    tasks = source.get_tasks()

    assert isinstance(tasks, Iterable)
    assert len([task for task in tasks]) == count
