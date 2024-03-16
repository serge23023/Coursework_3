import json
import os

from src.operation import Operation


def open_json(file_name: str) -> list:
    """
    Открывает и загружает JSON-файл.
    """
    with open(find_file(file_name), 'r', encoding='utf-8') as f:
        return json.load(f)


def find_file(filename):
    """
    Поиск файла по наименованию
    :return: Путь до файла
    """
    for root, dirs, files in os.walk(os.path.dirname(os.getcwd())):
        if filename in files:
            return os.path.join(root, filename)
    return None


def operations_create() -> list[Operation]:
    """
    Функция operations_create создает список операций, каждая из которых представляет собой объект Operation,
    и возвращает отсортированный список этих операций. Если элемент пуст, он пропускается.
    Ключи в словаре item изменяются перед созданием объекта Operation.
    """
    operations = []
    for item in open_json('operations.json'):
        if not item:
            continue
        item['operation_id'] = item.pop('id')
        item['operation_amount'] = item.pop('operationAmount')
        item['from_account'] = item.pop('from', None)
        operations.append(Operation(**item))
    operations.sort(key=lambda operation: operation.date, reverse=True)
    return operations


def print_operation(count: int):
    list_operation = []
    for operation in operations_create():
        if len(list_operation) < count and operation.state == "EXECUTED":
            list_operation.append(operation)
        elif len(list_operation) == count:
            break
    return list_operation
