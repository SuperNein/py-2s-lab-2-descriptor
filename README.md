# Лабораторная работа 1

**Источники задач и контракты**

---

## Цель работы

- Освоить duck typing и контрактное программирование на примере источников
задач.

---

## Структура проекта 

```
py-2s-lab-1-contract
│   .gitignore
│   .pre-commit-config.yaml
│   pyproject.toml
│   README.md
│   requirements.txt
│   
├───examples
│       main.py
│       tasks.json
│       __init__.py
│           
├───src
│   │   loader.py
│   │   models.py
│   │   protocols.py
│   │   validation.py
│   │   __init__.py
│   │   
│   ├───common
│   │       constants.py
│   │       __init__.py
│   │           
│   └───sources
│           API_stub_source.py
│           file_source.py
│           generator_source.py
│           __init__.py
│           
└───tests
    │   conftest.py
    │   test_loader.py
    │   test_validation.py
    │   __init__.py
    │   
    └───sources
            conftest.py
            test_API_stub_source.py
            test_file_source.py
            test_generator_source.py
            __init__.py
```

---

## Установка

### Установка и тесты

```
# Установка зависимостей
pip install -r requirements.txt

# Запуск examples
python -m examples.main

# Покрытие тестами
pytest tests/ --cov=src/ --cov-report=term-missing
```

### Библиотеки

- pytest

---

## Реализация

### Модель Task

Пользовательский класс, сожержащий необходимую минимальную информацию:
- id — уникальный идентификатор задачи
- payload — произвольные данные задачи

### Контракт источников

Все источники реализуют единый метод:

```
get_tasks() -> Iterable[Task]
```

### Источники

- Задачи, загружаемые из JSON файла
- Задачи, генерируемые программно (генератор)
- Задачи, получаемые из API-заглушки (под API-заглушкой понимается упрощённый программный компонент, имитирующий внешний источник задач)

---

## Выводы

В ходе работы я освоил:
- Принципы duck typing 
- Принципы контрактного программирования
- Тестирование с помощью мокирования поведения