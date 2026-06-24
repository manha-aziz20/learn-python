age=int(input("enter your age:"))
if age < 18:
    print("young")

if age >= 18:
    print("adult") 

if age >= 50:
    print("senior")

password=str(input("enter your password:"))
if len(password) >= 8:
    print("strong password")

if len(password) < 8:
    print("weak password")
