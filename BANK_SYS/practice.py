"""p=int(input("enter the principal amount  : "))
r=int(input("enter the rate percentage : "))
t=int(input("enter the time : "))
c=((p*r*t)/100)
a=(p+c)
print("your simple interest will be ",c)
print("your total amount to be paid will be ",a)"""

a=int(input())
if a>0:
    print("positive number")
elif a==0:
    print("zero")
else:
    print("negative number")