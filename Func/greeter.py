def get_formatted_name(first_name, last_name):
    """returns a clean name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nPlease input you name:")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello " + formatted_name + "!")
