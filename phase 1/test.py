#Question 1
city="Paris"
population= 6000

print("data type of city is:", type(city))
print("data type of population is:", type(population))

#Question 2
temp= float(input("enter temprature in celsius:"))
ans=(temp*9/5)+32
print(f"after converting into farenheit temp is {ans}")

#Question 3
x=15
y=4
remainder= x%y
print(remainder==0)
print(f"x is not perfectly divisible by y and the remainder is {remainder}")

#Question 4
full_name= input("enter your full name:")
print(len(full_name))
print(full_name.title())

#Question 5
a="python"
b="is"
c="awesome"
print(a,b,c, sep="-",end="!")