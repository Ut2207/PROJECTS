#VERSION1.1 OF STUDENT GRADE MANAGER
#IAM GOING TO POLISH THE CLI INTERFACE A BIT AND THEN WE CAN MOVE ON TO GUI AFTERWARDS VIA TINKER
#SINCE THE CODE IS MODULAR IN NATURE ADDINF MORE FEATURES ISNT THAT DIFFICULT
import json
students={}

def save_data():
    with open("students.json", "w") as file: 
        json.dump(students, file, indent=4)

def load_data():
    global students

    with open("students.json", "r") as file:
        students = json.load(file)


def add_marks():
    print("ENTER MARKS OF YOUR TOP FIVE SUBJECTS : ")
    name=input("ENTER STUDENT NAME:",)
    roll_no=int(input("ROLL_NO : " ,))
    maths=float(input("MATHS : " , ))
    physics =float(input("PHYSICS : ",))
    chemistry=float(input("CHEMISTRY : ",))
    english=float(input("ENGLISH : "),)
    computer_science=float(input("computer_science : ",))
    students[str(roll_no)]={
        "name":name,
        "marks":{
            "maths":maths,
            "physics":physics,
            "chemistry":chemistry,
            "english":english,
            "computer_science":computer_science,
        }
    }    
    save_data()


def del_rec():
    roll=input("ENTER ROLL NUMBER : ",)
    if roll in students:
        del students[roll]
        print("RECORD DELETED")
    else:
        print("RECORD NOT FOUND")
    save_data()

#TODO : when you make the interface() function make sure to remove the load data func from the del_rec() or any others and add it onece in the starting of the interface :)
def see_rec():
    roll=input("ENTER ROLL NUMBER OF THE STUDENT : ",)
    if roll in students:
        print(json.dumps(students[roll],indent=4))
    else:
        print("RECORD NOT IN DATABASE")


def avg_marks(roll_number):
    total=0
    count=0
    for marks in students[str(roll_number)]["marks"].values():
        total+=marks
        count+=1
    return float(total/count)


def show_topper():
    highest_average=0
    topper=''
    for rollno in students:
        current=avg_marks(rollno)
        if current>highest_average:
            highest_average=current
            topper=rollno
        else:
            continue
    return (topper,highest_average)

        

def class_average():
    summation=0
    count=0
    for student in students:
        summation+=avg_marks(student)
        count+=1 
    return summation/count 

def interface():
    load_data()
    print("==== WELCONE TO THE STUDENT GRADE MANAGER ====")
    print("1.ADD A RECORD")
    print("2.DELETE A RECORD")
    print("3.SEE A RECORD ")
    print("4.RETRIVE AVERAGE MARKS FOR A STUDENT")
    print("5.FIND THE TOPPER")
    print("6.CALCULATE CLASS AVERAGE")
    print("7.CLOSE")
    choice=int(input("WHAT DO YOU WANT TO DO [1-7] : "))
    if choice==1:
        add_marks()
        return True
    elif choice==2:
        del_rec()
        return True
    elif choice==3:
        see_rec()
        return True
    elif choice==4:
        roll_number=int(input("ENTER THE ROLL NUMBER OF THE STUDENT WHOSE AVERAGE IS TO BE RETRIVED : ",))
        print("THE AVERAGE MARKS : ",avg_marks(roll_number))
        return True
    elif choice==5:
        print(show_topper())
        return True
    elif choice==6:
        print("CLASS AVERAGE : ",class_average())
        return True
    else:
        print("LOGGING OFF")
        return False
try:
    load_data()
except:
    print("THIS FILE DOSENT EXIST")
while True:
    if not interface():
        break












