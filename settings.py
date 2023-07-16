from pathlib import Path
import json

CURRENT_PATH = Path(__file__).parent
PATH_WITH_FIXTURES = Path.joinpath(CURRENT_PATH, 'operations.json')


def get_data(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


data = get_data(PATH_WITH_FIXTURES)

print(data)
