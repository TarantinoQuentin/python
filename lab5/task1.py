import json


def task() -> float:
    with open('input.json', encoding='utf-8') as file:
        data = json.load(file)
        result = 0
        for block in data:
            result += round((block['score'] * block['weight']), 3)
    return result


print(task())
