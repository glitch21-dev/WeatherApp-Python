#CALCULATOR APP IN PYTHON USING USER INPUT CLASSES AND IF STATEMENTS

#Essentially we arejust declarating variables that prompt user input
operator = input("Enter an operator(+ - * /): ")
num1 = float(input("Enter 1st number: ")) #Using type casting to change the datatype of our numbers
num2 = float(input("Enter 2nd number: "))
#using string concatenation to print out our two variables together
#print(num1 + num2) but we use if statements to give the illusion of decison making
#The round() function can be used ti round off each of these
if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")