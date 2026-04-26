# Take input from the user
num = int(input("Enter a number: "))

# Initialize variables
factorial = 1
i = 1

# Check for negative number
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    # Calculate factorial using while loop
    while i <= num:
        factorial *= i
        i += 1

    print("Factorial of", num, "is:", factorial)