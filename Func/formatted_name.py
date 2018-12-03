'''
# 函数的返回值
def get_formatted_name(first_name, last_name):
    """return full name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


formatted_name = get_formatted_name('tom', 'wang')
print("\nHello, " + formatted_name + "!")
'''
# 让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musian = get_formatted_name('lisa', 'wang')
print(musian)
musian = get_formatted_name('lisa', 'wang', 'JK')
print(musian)
