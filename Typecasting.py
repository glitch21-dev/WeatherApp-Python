#TYPE CASTING IN PYTHON PRACTICE
#this is changing the value of one data type of one variable to another
#to do this we use the type() function by parsing it into a print statement
#

name = "Pirila Banda"
age = 21
gpa = 1.9
student = True

print(type(name)) #this returns the data type of the variable name
print(type(age))
print(type(gpa))
print(type(student))

#So now we use this technique to convert the data type of the variable age to whatever we choose
age = float(age)
print(age)
gpa = int(gpa)
print(gpa)
student = str(student)
print(student)

if student:
    print("You are a student")
else:
    print("You are not a student")