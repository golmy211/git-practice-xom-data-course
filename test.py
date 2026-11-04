print("line1\nline2")
print("line1\tline2")
print("LE VIET TIN\nK12\n23")
print("LE VIET TIN\tK12\t23")
print("Models\\raw\\sales.csv")
print("It's a terrible day")
print("He said \"OK\"")
print('He said "OK"')

# This is a line comment
""" this is a multi-line comment
used for long descriptions 
"""

print("Name:","Tin","AGE:",23)
print(1,2,3,4,5)
print(list(range(10)))
print("Name: Tin\n"
      "AGE: 23")
print("Name:Tin\nAge:23")
print("Name: Tin\n")
print("Total:", 10+20)

print("A" , "B" , "C", sep = "-")
print("A", "B", "C", sep = "/")
print("Le Viet Tin", end = " " )
print("23")
for i in range(5):
    print(i, end = "\n") # default end = "\n"

score = 4 
if score >= 5:
    print("Pass")
else:
    print("Fail")

total_score = (100+200.2 +
               300 + 400)
print(type(total_score))

_test_naming_convention = [1,2,10,3,4,5]
print(len(_test_naming_convention))

print(f"Total score:{total_score:,.2f}")

#Multiple assignments 

name,age,score = "Tin",23,9.5
x = y = z = 0 
print(name,age,score, sep = ",")

#SWAP VALUES 
name,age = age,name
print(name)
del score 
del x,y,z

#Unpacking list and tuple 
x = [1,2,3] 
print(x[0])
a,b,c = x 
print(f"a:{a}, b:{b}, c:{c}", sep = '-')

#tuple unpacking 
y = (4,5,6) 
name,age,score = y 
print(f"name:{name}")

#check existence of variable 
try:
    print(scoree)
except NameError:
    print("No")

print(type(y))
z = (6)
print(type(z))
y = ([4,5],6) 
print(type(y))
y[0].append(9)
print(y)