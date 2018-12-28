cars = ['bmw', 'benz', 'audi', 'toyota', 'subaru']

# permanently sort the list
# cars.sort()
# print(cars)

# lists are permanently inverted sorted
# cars.sort(reverse=True)
# print(cars)

# sorted list temporary sort
#newcars = sorted(cars)

newcars = []
while True:
    popedcars = cars.pop()
    newcars.append(popedcars.title())
    print(newcars)
    # 判断列表的长度
    if len(cars) == 0:
        print(cars)
        print(sorted(newcars))
        print(newcars)
        # 倒着打印列表
        newcars.reverse()
        print(newcars)
        break
