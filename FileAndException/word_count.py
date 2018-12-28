def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        #msg = "The file " + filename + " does not exist!"
        # print(msg)
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words")


filenames = ['programming.txt', 'guest.txt', '1.txt']
for filename in filenames:
    count_words(filename)
