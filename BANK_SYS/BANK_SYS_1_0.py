import random


def simple_intrests(s, r, t):
    return s * r * t / 100


def compound_intrest(p, r, t, n):
    return p * (1 + r / n) ** (n * t)


def calculate_FD():
    p = float(input("ENTER THE AMOUNT YOU HAVE DEPOSITED : "))
    r = 8
    t = int(input("ENTER THE AMOUNT OF TIME THATS HAS PASSED : "))
    deposit = 0
    for i in range(t):
        deposit = p * r / 100
        p = deposit

    print("THE AMOUNT YOU HAVE ACCUMULATED IN THE FD IS : ", deposit)


def remaining_amount():
    print("CHOOOSE WHCH TYPE OF INTREST WHERE YOU BOUND TO ??")
    print("1.SIMPLE INTREST")
    print("2.COMPOUND INTREST")
    choice = int(input())
    if choice == 1:
        p = float(input("PRINCIPAL :"))
        r = float(input("RATE OF INTREST : "))
        t = float(input("TIME : "))
        print("THE SIMPLE INTREST IS : ", simple_intrests(p, r, t))


def loan_auth():
    credit_score = int(input("ENETER YOUR CREDIT SCORE : "))
    lelgal_status = input("ANY LEGAL COMPLICATIONS(Y/N): ")
    if lelgal_status == "Y":
        print("LOAN APPLICATIONS WILL BE AUTO DENIED ")

    else:
        if credit_score > 850 or credit_score < 0:
            print("INVALID CREDIT SCORE")
        elif 740 < credit_score < 850:
            print("DUE TO AN EXCEELENT CREDIT SCORE THE APPLICATION IS AUTOACCEPTED")
            print(
                "THE FOLLOWING IS YOUR SECURE LOGIN KEY FOR THE PORTAL : ",
                random.randint(1000000, 9999999),
            )
        elif 670 < credit_score < 739:
            print("THE LOAN APPLICATION IS AUTOACCEPTED AT OUR STANDARD INTREST RATES")
            print(
                "THE FOLLOWING IS YOUR SECURE LOGIN KEY FOR THE PORTAL : ",
                random.randint(1000000, 9999999),
            )
        elif 580 < credit_score < 669:
            print("THE APPLICATION WILL HAVE TO GO UNDER A MANUAL REVIEW PROCESS")
            print(
                "THE FOLLOWING IS YOUR SECURE LOGIN KEY FOR THE PORTAL : ",
                random.randint(1000000, 9999999),
            )
        else:
            print("THE LOAN APPLICATION IS AUTO DENIED ")


def interface():
    print("==ENTER YOUR CHOICE FROM THE FOLLOWING AVVORDING TO YOUR NEEDS==")
    print("1.CALCULATE FD")
    print("2.REMAINING AMOUNT TO BE PAID")
    print("3.LOAN AUTHORIZATION")
    print("4.QUIT PROCESS")
    choice = int(input("ENTER YOUR CHOICE : "))
    if choice == 1:
        calculate_FD()
        return True

    elif choice == 2:
        remaining_amount()
        return True

    elif choice == 3:
        loan_auth()
        return True

    elif choice == 4:
        print("LOGGING OFF")
        return False

    else:
        print("INVALID CHOICE OF OPTION")
        return True


interface()
try:
    if interface():
        interface()
except:
    print("LOGGING OFF")
