#arithmetic operators
a=10
b=20
print(a+b) 
print(a-b)
print(a*b)
c=a*b
print(c)
print(a/b) # a divided by b answer in float
print(b/a)
print(a%b) #modelus operator give us remainder
print(a**b) # a raised to the power of b
print(a//b) # divison gives answer in int

#relational operators
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

#assignment operators
a=b
print(a)
a+=b #a= a+b
print(a)
a-=b #a= a-b
print(a)
a*=b #a= a*b
print(a)
a/=b #a= a/b
print(a)
a%=b #a= a%b
print(a)
a**=b #a= a**B
print(a)
a//=b #a= a//b
print(a)

#logical operators
c=True
d=False
a=10
b=5
print(c and d)
print(c or d)
print(not c)
print("and operator :", (a>b) and (a<b))
print("or operator:", (a>b) or (b>a))
print("not operator:",  not (a<b))

#membership operators
name= "manha"
print("a" in name)
print("i" in name)
print("m" not in name)

#identity operators
a=10
b=10
print(a is b)
print(a is not b)
