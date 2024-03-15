import json

from src.operation import Operation


def open_json():
    with open('../data/operations.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def operations_create():
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
