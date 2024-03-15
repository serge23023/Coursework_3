from src.utils import operations_create


def print_operation():
    i = 0
    for operation in operations_create():
        if i < 5 and operation.state == "EXECUTED":
            print(f"{operation.date.strftime("%d.%m.%Y")} {operation.description}\n"
                  f"{operation.from_} -> {operation.to}\n"
                  f"{operation.operation_amount.amount} {operation.operation_amount.currency.name}\n")
            i += 1
        elif i == 5:
            break


if __name__ == '__main__':
    print_operation()
