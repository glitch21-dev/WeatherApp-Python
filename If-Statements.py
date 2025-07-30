#basic desicion making in programming can be made using if statements
print("Welcome To The Sign Up Sheet")
age = int(input("Please enter your age to signup: ")) #Using typecasting to ensure our user input is an integer and not a string like the default nonsense

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are signed up")
elif age < 0:
    print("You have not been born yet")
else:
    print("You are too young to sign up")