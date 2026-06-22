name= input("enter your name:")
print(f"welcome {name} to our website") 

age= input("enter your age:")
height= input("enter your height:")

print("your name is", name)
print("your age is", age)
print("your height is", height)

print("type of name is", type(name))
print("type of age is", type(age))
print("type of height is", type(height))


age=int(age)
height=float(height)

print("type of age after type casting", type(age))
print("type of height after type casting", type(height))

name=input("your name is:")
age=int(input("your age is:"))
height=float(input("your height is:"))

print("your name is", name , " type of name is", type(name))
print("your age is", age , "type of age is", type(age))
print("your height is", height, "type of height is", type(height))
