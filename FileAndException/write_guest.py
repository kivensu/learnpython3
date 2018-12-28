filename = 'guest.txt'
question_file_name = 'guest_question.txt'
with open(filename, 'a') as file_object_guest:
    with open(question_file_name, 'a') as file_object_guest_question:
        while True:
            guest_name = str(input("Please input your name: "))
            print("Hello! " + guest_name + " !")
            questions = str(input("Why you like it? Please tell me: "))
            file_object_guest.write(guest_name + "\n")
            file_object_guest_question.write(questions + "\n")
            if guest_name == "admin":
                break
