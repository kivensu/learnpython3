def build_person(first_name, last_name, age=''):
    """return a dictionaly"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jack', 'ma', age=2)
print(musician)
