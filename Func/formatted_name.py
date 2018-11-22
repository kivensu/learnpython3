'''
def get_formated_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formated_name('lisa', 's', 'wang')
print(musician)
musician_01 = get_formated_name('jack', 'ma')
print(musician_01)
'''


def get_formatted_name(first_name, last_name):
    """return full name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\n Please tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = str(input("First name: "))
    if f_name == 'q':
        break

    l_name = str(input("Last name: "))
    if l_name == 'q':
        break

formatted_name = get_formatted_name(f_name, l_name)
print("\nHello, " + formatted_name + "!")
