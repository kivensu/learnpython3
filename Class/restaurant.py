class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is: " + self.restaurant_name)
        print("The restaurant cuisine is: " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is open!")


restaurant = Restaurant('lisa&bar', 'chinese food')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant01 = Restaurant('tom&bar', 'japan food')
restaurant01.describe_restaurant()
restaurant01.open_restaurant()

restaurant02 = Restaurant('jack&bar', 'dubai food')
restaurant02.describe_restaurant()
restaurant02.open_restaurant()
