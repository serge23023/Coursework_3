import json

from src.operation import Operation


def open_json() -> list:
    """
    Открывает и загружает JSON-файл.
    """
    with open('../data/operations.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def operations_create() -> list[Operation]:
    """
    Функция operations_create создает список операций, каждая из которых представляет собой объект Operation,
    и возвращает отсортированный список этих операций. Если элемент пуст, он пропускается.
    Ключи в словаре item изменяются перед созданием объекта Operation.
    """
    operations = []
    for item in open_json():
        if not item:
            continue
        item['operation_id'] = item.pop('id')
        item['operation_amount'] = item.pop('operationAmount')
        item['from_account'] = item.pop('from', None)
        operations.append(Operation(**item))
    operations.sort(key=lambda operation: operation.date, reverse=True)
    return operations
