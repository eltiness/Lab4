# TODO решите задачу
def task(file) -> float:
    sum=0
    count = 0
    with open(file, 'r') as f:
        data = json.load(f)
        for i in data:
            sum += i['score'] * i['weight']
    return round(sum, 3)
import json
file='input.json'

print(task(file))
