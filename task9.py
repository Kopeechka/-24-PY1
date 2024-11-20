import json

def task() -> float:
    with open('input.json', 'r') as file:
        json_data = json.load(file)

    total_sum = sum(item['score'] * item['weight'] for item in json_data)

    rounded_sum = round(total_sum, 3)
    return rounded_sum

print(task())
