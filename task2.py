# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as f:
        with open(OUTPUT_FILENAME, 'w') as g: # TODO считать содержимое csv файла
            input = csv.DictReader(f)
            columns = [row for row in input]
            json.dump(columns, g, indent=4) # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
