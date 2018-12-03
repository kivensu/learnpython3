magicians = ['tom', 'lisa', 'jack', 'luffy']


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    new_magician = []
    while True:
        poped_magican = magicians.pop()
        new_magician.append("The Great " + poped_magican)
        if len(magicians) == 0:
            break
    return new_magician


show_magicians(magicians[:])
magic = make_great(magicians[:])
print(magic)
print(magicians)
