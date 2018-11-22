'''
user_list01 = ['Admin', 'a', 'a', 'b', 'd']
for user in user_list01:
	if user.title() == 'Admin':
		print ("Hello " + user.title() + "," + " would you like to see a status report!")
	elif len(user_list01) == 0:
		print ("We need to find some users!")
	else:
		print ("Hello " + user.title() + "," + " thank you log in again")
'''

current_users = ['Admin', 'root', 'jenkins', 'docker', 'dhcp', 'print']
new_users = ['Admin', 'lisa', 'tom', 'jenkins', 'jack']
for user in new_users:
    if user not in current_users:
        print("\nThis user " + user + " not used!")
    else:
        print("\nThis user " + user + "has been used!")
        print("Please input another user: ")
