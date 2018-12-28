# positional arguments
def describe_pet(animal_type, pet_name, animal_age=13):
    """display animal info"""
    print("\nI love a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() +
          "." + " It's " + str(animal_age) + " year's old!")


# 调用多次函数 位置实参的顺序很重要！
describe_pet('hamster', 'tom')
describe_pet('dog', 'jack')

# 关键字实参
describe_pet(animal_type='fish', pet_name='jerry')
describe_pet(animal_type='cat', pet_name='tom')

# 只要函数能生成你希望的输出就OK了！证明函数调用成功了！

describe_pet()
