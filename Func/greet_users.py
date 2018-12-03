# 向函数传递列表，效率很高！
def greet_users(names):
    """greet every users"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['lisa', 'tom', 'jack', 'jerry']
greet_users(usernames)
