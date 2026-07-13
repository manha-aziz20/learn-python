# #Question 1
# number=int(input("enter a number:"))
# if number>0:
#     print("the number is postivie")
# if number==0:
#         print("number is zero")
# else:
#     print("number is negative")

# #Question 2
# marks=int(input("enter your marks:"))
# if marks>50:
#      print("Pass")
# else:
#      print("Fail")

#Question 3
temp=int(input("enter temprature in celsius:"))
if temp<0:
     print("Freezing")
elif temp>0 and temp<=15:
     print("Cold")
elif temp>=16 and temp<=25:
     print("Comfortable")
elif temp>=26 and temp<=35:
     print("Warm")
elif temp>35:
     print("Hot")

#Question 4
age=int(input("enter your age:"))
license= input("do you have a drivers license yes/no:").lower()
if age>=18:
     if license=="yes":
          print("you can drive")
if age>= 18:
     if license=="no":
          print("you need a license to drive")
if age<18:
     print("You are too young to drive")

#Question 5
day= int(input("enter a day 1-7:"))
match day:
     case 1:
          print("Monday")
     case 2:
          print("tuesday")
    
