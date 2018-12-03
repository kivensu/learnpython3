def city_country(city_name, country_name):
    city_info = '"' + city_name.title() + "," + country_name.title() + '"'
    return city_info


city_01 = city_country('beijing', 'china')
city_02 = city_country('hanzhou', 'china')
city_03 = city_country('newyork', 'USA')
print(city_01, city_02, city_03)
