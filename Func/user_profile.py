def build_profile(first, last, **user_info):
    """create a dict include user_info"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_info = build_profile('lisa', 'wang', location='beijing')
print(user_info)
my_info = build_profile('kiven', 'su', location='beijing',
                        hobby='swimming', like='computer')
print(my_info)


def make_car(maker, model, **car_info):
    car_infos = {}
    car_infos['maker'] = maker
    car_infos['model'] = model
    for key, value in car_infos.items():
        car_infos[key] = value
    return car_infos


my_car_info = make_car('audi', 'A4', color='red')
print(my_car_info)

"""
class car():
    #car test

    def __init__(self, maker, model):
        self.maker = maker
        self.model = model

    def make_car(self, maker, model, ** car_info):
        car_infos = {}
        car_infos['maker'] = self.maker
        car_infos['model'] = self.model
        for key, value in car_infos.items():
            car_infos[key] = value
        return car_infos


my_car = car.make_car('A', 'audi', 'A4', color='red')
print(my_car)
"""