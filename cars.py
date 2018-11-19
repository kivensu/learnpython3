cars = ['bmw', 'benz', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

#newcars = sorted(cars)
newcars = []
while True:
    popedcars = cars.pop()
    newcars.append(popedcars.title())
    print(newcars)
    if len(cars) == 0:
        print(cars)
        print(sorted(newcars))
        print(newcars)
        newcars.reverse()
        print(newcars)
        break
