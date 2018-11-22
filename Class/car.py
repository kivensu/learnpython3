class Car():

    def __init__(self, make, model, year):
        """init """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def get_odomete(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This car has a big gas tank!")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """init"""
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWH battery!")

    def fill_gas_tank(self):
        print("this car doesn't need  a gas tank!")


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWH battery!")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range == 270

        message = "This car can go to approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
