cars = ['bmw', 'benz', 'audi', 'toyota', 'subaru']

# sort对列表进行永久排序
# cars.sort()
# print(cars)

# 永久列表反排
# cars.sort(reverse=True)
# print(cars)

# sorted对列表进行临时排序
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
