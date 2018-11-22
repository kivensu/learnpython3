from name_function import get_formatted_name

print("Enter 'q' at any time to quit!")
while True:
    first = input("\nPlease input you first name :")
    if first == 'q':
        break
    last = input("Please input you last name: ")
    if last == 'q':
        break

    format_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + format_name + '.')
