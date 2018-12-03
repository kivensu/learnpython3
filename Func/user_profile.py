# 接收任意数量的关键字实参
def build_profile(first, last, **user_info):
    """create a dict include user_info"""
    # **user_info创建了一个空字典
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
