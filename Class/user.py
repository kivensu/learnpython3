class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("user full name is: " + self.first_name + self.last_name)

    def greet_user(self):
        print("hello " + self.first_name)


user01 = User('lisa', 'wang')
user01.describe_user()
user01.greet_user()

user02 = User('tom', 'liu')
user02.describe_user()
user02.greet_user()

user03 = User('jack', 'ma')
user03.describe_user()
user03.greet_user()
