age = int(input("Please input your age: "))
if age < 2:
    print("your are little enough!")
elif age >= 2 and age < 4:
    print("Your are little child!")
elif age >= 4 and age < 13:
    print("Your are child!")
elif age >= 13 and age < 20:
    print("You are young people!")
elif age >= 20 and age < 65:
    print("Your are adult!")
elif age >= 65:
    print("Your are old enough!")
