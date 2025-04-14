import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with (open(INPUT_FILENAME, encoding='utf-8') as input_file,
          open(OUTPUT_FILENAME, 'w', encoding='utf-8') as output_file):
        json_data = [row for row in csv.DictReader(input_file)]

        json.dump(json_data, output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
