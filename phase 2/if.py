age=int(input("enter your age:"))
if age < 18:
    print("young")

if age >= 18:
    print("adult") 

if age >= 50:
    print("senior")

password1=str(input("enter your password:"))
if len(password1) >= 8:
    print("strong password")

if len(password1) < 8:
    print("weak password")

username=input("enter your username:")
password=input("enter your password:")
if username == "admin":
    if password=="1234":
        print("login succesfull")
    else:
        print("incorrect password")
else:
    print("username incorrect")

marks=int(input("enter your marks:"))
attendance=int(input("enter your attendance:"))
if marks>=50:
    if attendance>=75:
        print("you passed and are eligible for certificate")
    else:
        print("you passed but are not eligible for certificate")
else:
    print("you havent passed")
            
balance=int(input("enter your amount:"))
amount=int(input("enter your amount:"))
if balance>0:
    if amount>balance:
        print("insufficient amount for withdrawal")
    else:
        print("you can place withdrawal")
else:
    print("no balance")
