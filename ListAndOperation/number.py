# use range print some number
# for value in range(1, 11):
#    print(value)

# use range create even number list
#numbers = list(range(1, 6))
# print(numbers)

# use range create list
# even_numbers
#even_numbers = list(range(0, 11, 2))
# print(even_numbers)


# even squares(1-10)
'''
squares = []
for value in range(1, 11):
    square = value ** 2
    if square % 2 == 0:
        squares.append(square)

print(squares)
'''

# digit
# simple staticstics
'''
digits = [1, 123, 1, 4, 13, 1, 42, 2112]
print(min(digits))
print(max(digits))
print(sum(digits))
'''

# list analysis
#squares = [value ** 2 for value in range(0, 101, 2)]
# print(sum(squares))

#list01 = list(range(1, 1000001))
# print(min(list01))
# print(max(list01))
# print(len(list01))
# print(sum(list01))

'''
list01 = list(range(1, 20, 2))
print(list01)
for x in list01:
    print(x)
'''

#list02 = [value % 3 == 0 for value in range(3, 31)]
# print(list02)
# for x in list02:
#    print(x)


'''
list02 = list(range(3, 31))
for x in list02:
    if x % 3 == 0:
        print(x)
'''

# cube list analysis
'''cubes list
cubes = [value ** 3 for value in range(1, 11)]
for x in cubes:
    print(x)
'''
