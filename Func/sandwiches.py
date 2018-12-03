def get_sandwiches(*toppings):
    print("\nThis sandwiches include: ")
    for topping in toppings:
        print("-" + topping)


get_sandwiches('tomato', 'potato', 'fish')
get_sandwiches('tomato', 'cheese', 'potato', 'tuna fish')
