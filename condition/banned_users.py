banned_users = ['tom', 'jack', 'robin', 'david']
user = 'jack'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish!")
else:
    print(user.title() + ", sorry!")
