
day= int(input("enter a day (1-7):"))
if day== 1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wednesday")
elif day==4:
    print("thursday")
elif day==5:
    print("friday")
elif day==6:
    print("saturday")
elif day==7:
    print("sunday")
else:
    print("invalid day")

# #practise 2
# grade= int(input("enter your marks:"))
# #if grade 





# get 2 numbers from uesr if their sum is greater 10 then sum multiply with 5 if their sum is greater 20 then sum multiply with 10
# if their sum is greater 30 then sum multiply with 30 if sum is equal to 30 then multiply with 50
number1=int(input("enter a number:"))
number2=int(input("enter a number:"))
sum = number1 + number2
if sum > 30:
    print((sum)*30)
elif sum == 30:
    print((sum)*50)
elif sum >20:
    print((sum)*10)
elif sum > 10:
    print((sum)*5)
