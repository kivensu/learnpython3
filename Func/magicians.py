magicians = ['tom', 'lisa', 'jack', 'luffy']


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    poped_magican = magicians.pop()
    new_magician = []
    new_magicians = new_magician.append("The Great " + poped_magican)
    print(new_magicians)


while True:
	poped_magican = magicians.pop()
    print(poped_magican)
    if len(magicians) == 0:
    	break
