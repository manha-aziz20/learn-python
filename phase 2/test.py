#Question 3
score=int(input("enter your score:"))
if score>=90:
    print("A+")
elif score>=80:
    print("A")
elif score>=70:
    print("B")
elif score>=60:
    print("C")
elif score>=50:
    print("D")
elif score<50:
    print("F")

#Question 4
balance=int(input("enter your balance:"))
withdraw=int(input("how much do u want to withdraw:"))
if balance<=0:
    if withdraw<=balance:
        print("Withdrawal succesfull")
    if withdraw>=balance:
        print("insufficient balance")
else:
    print("invalid statement")
    
