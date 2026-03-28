# Лабораторная работа 2

**Модель задачи: дескрипторы и @property**

---

## Цель работы

-  Освоить управление доступом к атрибутам и защиту инвариантов доменной модели.

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
│       tasks.json
│           
├───src
│   │   main.py
│   │   __init__.py
│   │   
│   ├───common
│   │       constants.py
│   │       __init__.py
│   │                
│   ├───core
│   │       descriptors.py
│   │       enums.py
│   │       exceptions.py
│   │       models.py
│   │       __init__.py
│   │   
│   ├───protocols
│   │       sources.py
│   │       __init__.py
│   │
│   ├───services
│   │       loader.py
│   │       validation.py
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
python -m src.main

# Покрытие тестами
pytest tests/ --cov=src/ --cov-report=term-missing
```

### Библиотеки

- pytest

---

## Реализация

### Модель Task

Пользовательский класс с атрибутами:
- id — уникальный идентификатор задачи
- payload — произвольное описание задачи
- priority - приоритет
- status - статус задачи
- created_at - время создания
- is_closed - статус закрытия задачи

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
- Работу с доступом к атрибутам
- Принцип работы data и non-data descriptors