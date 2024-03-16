import pytest
from src.operation import Operation
from src.utils import open_json, operations_create, print_operation


def test_open_json():
    # Проверка, что функция open_json возвращает список
    assert type(open_json('operations.json')) is list
    with pytest.raises(TypeError):
        open_json('perations.json')


def test_operations_create():
    operations = operations_create()
    # Проверка, что функция operations_create возвращает список
    assert type(operations) is list
    # Проверка, что все элементы в списке являются экземплярами класса Operation
    assert all(isinstance(operation, Operation) for operation in operations)


def test_print_operation(i):
    operations = print_operation(i)
    assert len(operations) == i
    for operation in operations:
        assert operation.state == "EXECUTED"


# Запуск тестов с помощью pytest
if __name__ == "__main__":
    pytest.main()
