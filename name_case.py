username = str(input("Please input you name: "))
famous_person = str(input("Please input you favorite famous person name: "))
print("Hello " + username + ", " + "would you like learn some Python today?")
print("Hello " + username.title() + "," +
      "would you like learn some Python today?")
print("Hello " + username.upper() + "," +
      "would you like learn some Python today?")
print("Hello " + username.lower() + "," +
      "would you like learn some Python today?")
message = famous_person + \
    " once said,'A person who never made a misitake never tried anything new!'"
print(message)
people_name = str(input("Please input an name: "))
print(people_name.lstrip())
print(people_name.rstrip())
print(people_name.strip())
