def describe_pet(animal_type, pet_name, animal_age=13):
    """display animal info"""
    print("\nI love a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'tom')
describe_pet('dog', 'jack')
describe_pet(animal_type='fish',pet_name='jerry')
