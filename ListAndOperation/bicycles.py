# 打印列表
bicycles = ['creak', 'cannondale', 'trip', 'alex']
print(bicycles)

# 列表索引
# print(bicycles[0])
# print(bicycles[1])
# print(bicycles[-1])
print("My first bicycles is " + bicycles[0].title() + " !")

# 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# motorcycles[0] = 'ducadi'
# print(motorcycles)

# 在列表末尾添加元素
# motorcycles.append('dukadi')
# print(motorcycles)

# 在列表中插入元素
# motorcycles.insert(0, 'dukati')
# print(motorcycles)

# 使用del语句删除列表元素
#del motorcycles[0]
# print(motorcycles)
#del motorcycles[1]
# print(motorcycles)

# 使用pop方法删除列表元素
#poped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(poped_motorcycles)

#last_owned = motorcycles.pop()
# print("The last motorcycle I owned was a " + last_owned.title() + " .")
# print(motorcycles)

# pop很强！
#first_owned = motorcycles.pop(0)
# print('The first motorcycle I owned was a ' + first_owned.title() + '!')

# motorcycles.remove('yamaha')
# print(motorcycles)

# 根据值删除列表元素
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print("\nA" + too_expensive.title() + "is too expensive for me!")
# print(motorcycles)
