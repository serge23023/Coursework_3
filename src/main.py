from src.utils import operations_create


def print_operation():
    """
    Выводит представление первых пяти выполненных операций.
    """
    i = 0
    for operation in operations_create():
        if i < 5 and operation.state == "EXECUTED":
            print(operation.__repr__())
            i += 1
        elif i == 5:
            break


if __name__ == '__main__':
    print_operation()
