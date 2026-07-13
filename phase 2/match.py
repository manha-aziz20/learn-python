day= int(input("enter a day 1-7:"))
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid day")    

num1=int(input("enter a number:"))
num2=int(input("enter your number:"))
op=input("==,+,-,*,%:")
match op:
    case "+":
        print("your result is:", num1 + num2)
    case"-":
        print("your result is:", num1 - num2)
    case"*":
        print("your result is:", num1 * num2)