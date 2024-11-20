import json

def task() -> float:
    filename = 'input.json'
    with open(filename, 'r') as f:
        json_data = json.load(f)

    total_sum = sum(item['score'] * item['weight'] for item in json_data)

    return round(total_sum, 3)

print(task())
