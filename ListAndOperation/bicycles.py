# print list
bicycles = ['creak', 'cannondale', 'trip', 'alex']
print(bicycles)

# list indexes
# print(bicycles[0])
# print(bicycles[1])
# print(bicycles[-1])
print("My first bicycles is " + bicycles[0].title() + " !")

# change list element
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# motorcycles[0] = 'ducadi'
# print(motorcycles)

# in list tail add element
# motorcycles.append('dukadi')
# print(motorcycles)

# element insert into list 
# motorcycles.insert(0, 'dukati')
# print(motorcycles)

# use del delete list element
#del motorcycles[0]
# print(motorcycles)
#del motorcycles[1]
# print(motorcycles)

# use pop delete list element
#poped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(poped_motorcycles)

#last_owned = motorcycles.pop()
# print("The last motorcycle I owned was a " + last_owned.title() + " .")
# print(motorcycles)

# pop is powerful!
#first_owned = motorcycles.pop(0)
# print('The first motorcycle I owned was a ' + first_owned.title() + '!')

# motorcycles.remove('yamaha')
# print(motorcycles)

# according to element value to delete
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print("\nA" + too_expensive.title() + "is too expensive for me!")
# print(motorcycles)
