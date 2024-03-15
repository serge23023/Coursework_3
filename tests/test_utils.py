import pytest
from src.operation import Operation
from src.utils import open_json, operations_create


def test_open_json():
    # Проверка, что функция open_json возвращает список
    assert isinstance(open_json(), list)


def test_operations_create():
    operations = operations_create()
    # Проверка, что функция operations_create возвращает список
    assert isinstance(operations, list)
    # Проверка, что все элементы в списке являются экземплярами класса Operation
    assert all(isinstance(operation, Operation) for operation in operations)


# Запуск тестов с помощью pytest
if __name__ == "__main__":
    pytest.main()
