# Take input from the user
age = int(input("Enter your age: "))
degree = input("Do you have a degree? (Yes/No): ")

# Nested if-else to check eligibility
if age >= 18:
    if degree.lower() == "yes":
        print("You are eligible for the job")
    else:
        print("You are not eligible (Degree required)")
else:
    print("You are not eligible (Must be 18 or older)")