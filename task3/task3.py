import sys
import json
# объявляем функцию, которая будет менять нужные значения, рекурсивно вызывая сама себя при обнаружении бОльшей глубины
def recursive_filling(tests, values):
    if isinstance(tests, dict):
        if 'id' in tests and tests['id'] in values:         # если встречаем просто словарь, то меняем значения
            tests['value'] = values[tests['id']]
        if 'values' in tests:                               #не придумал, как можно "заглубиться" без прямого обращения к ключу
            recursive_filling(tests['values'], values)
    elif isinstance(tests, list):       #для провала в первый список
        for el in tests:
            recursive_filling(el, values)

tests_path = sys.argv[1]
values_path = sys.argv[2]
report_path = sys.argv[3]

with open(tests_path) as file:
    tests_data = json.load(file)
with open(values_path) as file:
    values_data = json.load(file)

values_dict = {el['id']: el['value'] for el in values_data['values']}


recursive_filling(tests_data['tests'], values_dict)
print(tests_data)
with open(report_path, 'w') as file:
    json.dump(tests_data, file, indent=1)