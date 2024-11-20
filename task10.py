# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None: # считываем содержимое
    with open(INPUT_FILENAME, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    with open(OUTPUT_FILENAME, mode='w', newline='') as jsonfile:
        json.dump(data, jsonfile, indent=4)
# делим строчки с отступами

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
