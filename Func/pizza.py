# 收集任意数量的实参 使用位置实参+任意数量的实参
def make_pizza(size, *toppings):
    """print customer toppings"""
    print("\nMaking a " + str(size) + " pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
