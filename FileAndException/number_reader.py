import json
filename = 'number.json'
with open(filename) as file_obj:
    number = json.load(file_obj)
print(number)
