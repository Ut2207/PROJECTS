# VERSION1 OF STUDENT GRADE MANAGER
import json

students = {}


def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def load_data():
    global students

    with open("students.json", "r") as file:
        students = json.load(file)


def add_marks():
    print("ENTER MARKS OF YOUR TOP FIVE SUBJECTS IN ANY ORDER(SEPERATED BY SPACE)")
    name = input(
        "ENTER STUDENT NAME:",
    )
    marks = list(map(int, input("ENTER MARKS: ").split()))
    if name.lower() in students:
        print("THIS RECORD ALREADY EXISTS IN THE DATABASE")
    elif len(marks) != 5:
        print("FIVE SUBJECTS DAMM IT !!")
    else:
        students[name.lower()] = marks
    save_data()


def del_rec(student):
    student = student.lower()
    if student in students:
        del students[student]
        print("RECORDS DELETED")
    else:
        print("INPUT INVALID")
    save_data()


def see_rec(student):
    student = student.lower()
    if student in students:
        print("THE RECORD IS:", students[student])
    else:
        print("INVALID INPUT")


def show_topper():
    if len(students) == 0:
        print("NO RECORDS IN DATABASE")
        return
    maximum = 0
    topper = ""
    for student in students:
        total = sum(students[student])
        if total > maximum:
            topper = student
            maximum = total
    print("the topper is :", (topper))
    print("the percentage is :", sum(students[topper]) / 5)


def avg_marks(student):
    student = student.lower()
    if student in students:
        print("STUDENT NAME:", student, "AVG MARKS:", sum(students[student]) / 5)
    # TODO : ADD A CHOICE IF CHOICE = 'ALL' PRINT ALL RECORDS ELSE PRINT THE AVG_MARKS FOR THE PARTICULAR STUDENT
    else:
        print("INPUT INVALID")


def interface():
    print("""
    1)ADD RECORDS 
    2)DELETE RECORD 
    3)SEE RECORDS 
    4)SHOW TOPPER 
    5)AVERGAE MARKS 
    6) QUIT""")
    check_choice = int(
        input(
            "ENETR YOUR CHOICE:",
        )
    )
    if check_choice == 1:
        add_marks()
        return True
    elif check_choice == 2:
        if check_choice == int(check_choice):
            delete_record = input(
                "ENTER THE NAME OF THE UNFORTUNATE STUDENT:",
            )
            del_rec(delete_record)
            print("THE SYSTEM HAS ERASED THE UNFORTUNATE STUDENT")
            return True
        else:
            print("THE INPUT IS INVALID")
            return True
    elif check_choice == 3:
        if check_choice == int(check_choice):
            seeing_records = input(
                "ENTER THE NAME OF THE STUDENT WHOSE RECORD HAS TO BE SEEN : "
            )
            see_rec(seeing_records)
            return True
        else:
            print("PLEASE AT LEAST GIVE ME A VALID INPUT :(")
            return True
    elif check_choice == 4:
        show_topper()
        return True

    elif check_choice == 5:
        average_student = input(
            "ENTER THE NAME OF THE STUDENT WHOSE AVERGAE MARKS NEED TO BE RETRIVED:",
        )
        avg_marks(average_student)
        return True
    elif check_choice == 6:
        print("LOGGING OFF")
        return False
    else:
        print("INVALID INPUT")


# TODO: """1)MAKE THE INTERFACE IN A LOOP , 2)INPUT VALIDATION , 3) PREVENT DUPLICATES"""
try:
    load_data()
except:
    print("THIS FILE DOSENT EXIST")
while True:
    if not interface():
        break
# NOW WE ARE GOING TO ADD FUNCTION OF PERMANENTLY STORING IN A FILE  BY LEARNING JSON .
