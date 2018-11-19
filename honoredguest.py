guest_list = ['mengyao', 'jue', 'duoer']

print("Guest " + guest_list[1] + " doesn't come here!")
guest_list[1] = "lisa"
print("Welcome to here! " + guest_list[0])
print("Welcome to here!" + guest_list[1])
print("Welcome to here!" + guest_list[2])
print("I find a bigger table!,I hope invite more people come here!")
guest_list.insert(0, 'jue')
guest_list.insert(2, 'zhangjie')
guest_list.append('liuchang')
print(guest_list)

for name in guest_list:
    print("Welcome to here! " + name)
print("Sorry, I only invite two people come to here!")

# 栈的含义！
print(guest_list)
while True:
    poped_people = guest_list.pop()
    print("Sorry! " + poped_people + " ByeBye!")
    if len(guest_list) == 2:
        print(guest_list)
        print("hello! " + guest_list[0])
        print("hello!" + guest_list[1])
        del guest_list[1]
        del guest_list[0]
        print(guest_list)
        break
