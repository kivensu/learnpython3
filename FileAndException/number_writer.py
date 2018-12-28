import json
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filename = 'number.json'
with open(filename, 'a') as file_obj:
    json.dump(numbers, file_obj)
