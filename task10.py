import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None: # считываем содержимое
    with open(INPUT_FILENAME, "r") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    with open(OUTPUT_FILENAME,"w") as f:
        json.dump(data, f, indent=4)
# делим строчки с отступами

if __name__ == '__main__':
    # нужно для проверки...
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
