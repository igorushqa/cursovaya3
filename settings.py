from pathlib import Path

import json

CURRENT_PATH = Path(__file__).parent
PATH_WITH_FILES = Path.joinpath(CURRENT_PATH, 'operations.json')


def get_data(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


data = get_data(PATH_WITH_FILES)


def delete_empty_operations(operations):
    operations.remove({})
    return operations


new_data = delete_empty_operations(data)


def first_five_sorted_operations(operations_list):
    return sorted(operations_list,
                  key=lambda operation_data: (operation_data['state'], operation_data['date']),
                  reverse=True
                  )[:5]


five_operations = first_five_sorted_operations(new_data)
