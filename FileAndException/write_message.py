filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming!\n")
    file_object.write("I love creating a new games!\n")

with open(filename, 'a') as file_object01:
	file_object01.write("I also love finding meaning in large datasets.\n")