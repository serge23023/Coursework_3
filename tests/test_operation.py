from datetime import datetime

import pytest

from src.amount import Amount
from src.operation import Operation


def test_operation():
    amount = {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}
    operation = Operation(441945886, "EXECUTED", "2019-08-26T10:50:58.294041",
                          amount, "Перевод организации",
                          "Счет 64686473678894779589", "Maestro 1596837868705199")
    operation1 = Operation(441945886, "EXECUTED", "2019-08-26T10:50:58.294041",
                           amount, "Перевод организации",
                           "Счет 64686473678894779589")

    # Проверка атрибутов класса Operation
    assert operation.id == 441945886
    assert operation.state == "EXECUTED"
    assert operation.date == datetime.strptime("2019-08-26T10:50:58.294041", "%Y-%m-%dT%H:%M:%S.%f")
    assert isinstance(operation.operation_amount, Amount)
    assert operation.description == "Перевод организации"
    assert operation.to == "Счет **9589"
    assert operation.from_ == "Maestro 1596 83** **** 5199"
    assert operation1.from_ is None
    assert operation.__repr__() == ("26.08.2019 Перевод организации\n"
                                    "Maestro 1596 83** **** 5199 -> Счет **9589\n"
                                    "31957.58 руб.\n")
    assert operation1.__repr__() == ("26.08.2019 Перевод организации\n"
                                     "Счет **9589\n"
                                     "31957.58 руб.\n")


# Запуск теста с помощью pytest
if __name__ == "__main__":
    pytest.main()
