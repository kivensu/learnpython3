# 返回一个表示人的字典
def build_person(first_name, last_name, age=''):
    """return a dictionaly"""
    person = {'first': first_name.title(), 'last': last_name.title()}
    if age:
        person['age'] = age
    return person


musician = build_person('jack', 'ma', age=45)
print(musician)
