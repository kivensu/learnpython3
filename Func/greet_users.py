def greet_users(names):
    """greet every users"""
    for name in names:
        msg = "Heelo, " + name.title() + "!"
        print(msg)


usernames = ['lisa', 'tom', 'jack', 'jerry']
greet_users(usernames)
