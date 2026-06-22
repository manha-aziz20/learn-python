#string indexing
name = "manha"
print(name[0])
print(name[1])  
print(name[2])
print(name[3])
print(name[4])
print(len(name))

#string slicing
full_name = "manha aziz" 
print(full_name[::-1])
print(full_name[0::3])
print(full_name[1:-2:])

#concatination
name= "manha"
print(name + "aziz")
print(name + " aziz")
print(name * 2)
name="manha aziz"
print("a" in name)
print("p" in name *2)
print("r" in name)

#relational operators
print(name>"aziz")
print(name< "manha")
print(name=="manha")
print(name<='manha')
print(name>="manha")
print(name!="manha")

#string methods
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.index("a"))
print(name.count("m"))
print(" ".join(name))
print(name.find("a"))
print(name.swapcase()) #changes uppercase to lowercase and lowercase to uppercase
print(name.strip())
print(name.lstrip()) #removes space only from left side
print(name.rstrip())
