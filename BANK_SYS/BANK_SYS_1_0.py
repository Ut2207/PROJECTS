import random


def simple_intrests(s, r, t):
    return s * r * t / 100


def compound_intrest(p, r, t, n):
    return p * (1 + (r / 100) / n) ** (n * t)


def calculate_FD():
    p = float(input("ENTER THE AMOUNT YOU HAVE DEPOSITED : "))
    r = float(input("ENTER THE RATE OF INTREST YOU GOT ON YOUR FD : "))
    t = int(input("ENTER THE AMOUNT OF TIME THATS HAS PASSED : "))
    deposit = 0
    for i in range(t):
        deposit = p * r * 1 / 100
        p += deposit

    print("THE AMOUNT YOU HAVE ACCUMULATED IN THE FD IS : ", p)


def discount_cash_flows(cash_flows, discount_rate):
    """the function isnt advanced enough for major enterprise grade calculations
    although the math is the same the varation in situation increases so this will
    just compare things for the case when someine offers you a commodity and MONEY
    and we have to decide which ones more profitable ot us"""
    present_value = 0.0
    for i in range(len(cash_flows)):
        # Apply the discount factor for the i-th cash flow (time period i+1)
        present_value += cash_flows[i] / ((1 + discount_rate) ** (i + 1))
    return present_value


def remaining_amount():
    print("CHOOOSE WHCH TYPE OF INTREST WHERE YOU BOUND TO ??")
    print("1.SIMPLE INTREST")
    print("2.COMPOUND INTREST")
    choice = int(input("ENTER YOUR CHOICE : "))
    if choice == 1:
        p = float(input("PRINCIPAL :"))
        r = float(input("RATE OF INTREST : "))
        t = float(input("TIME : "))
        print("THE SIMPLE INTREST IS : ", simple_intrests(p, r, t))
        return True
    else:
        p = float(input("PRINCIPAL : "))
        r = float(input("RATE : "))
        t = float(input("TIME : "))
        n = int(
            input(
                "ENTER THE FRACTIOON OF THE YEAR THE COMPOUND INTREST HAS TO BE APPLIED TO : "
            )
        )
        print("THE COMPOUND INTREST IS : ", compound_intrest(p, r, t, n))
        return True


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
            )
        else:
            print("THE LOAN APPLICATION IS AUTO DENIED ")


def currency_conversion():
    "BY DEFAULT THE CURRCNY TYPE IS SET TO Rs"
    inr_conversion_dict = {
        "USD": 0.0104,  # US Dollar
        "EUR": 0.0089,  # Euro
        "GBP": 0.0076,  # British Pound
        "AED": 0.0384,  # UAE Dirham
        "AUD": 0.0146,  # Australian Dollar
        "CAD": 0.0144,  # Canadian Dollar
        "JPY": 1.6590,  # Japanese Yen
        "SGD": 0.0133,  # Singapore Dollar
        "CHF": 0.0083,  # Swiss Franc
        "MYR": 0.0422,  # Malaysian Ringgit
    }
    a = input("ENTER THE 3 LETTER FOR THE COUNTRY YOU WANT TO CONVER INTO : ")
    b = float(input("ENTER THE AMOUNT OF MONEY IN Rs YOU HAVE : "))
    print("THE CONVERSION IS : ", b * inr_conversion_dict[a])


def interface():
    print("==ENTER YOUR CHOICE FROM THE FOLLOWING AVVORDING TO YOUR NEEDS==")
    print("1.CALCULATE FD")
    print("2.REMAINING AMOUNT TO BE PAID")
    print("3.LOAN AUTHORIZATION")
    print("4.CURRENCY CONVERSION")
    print("5.DISCOUNTING CASH FLOWS")
    print("6.QUIT PROCESS")
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
        currency_conversion()
        return True

    elif choice == 5:
        n = int(input("ENTER THE AMOUNT OF CASH FLOWS YOU HAVE THE ENETR : "))
        l = []
        for i in range(n):
            a = float(input("PLESE ENTER THE CASH FLOW : "))
            l.append(a)

        b = int(input("PLEASE ENETER THE DISCOUNT RATE : "))
        c = discount_cash_flows(l, b)
        print("THE PRESENT VALUE IS : ", c)
        return True
    elif choice == 6:
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
