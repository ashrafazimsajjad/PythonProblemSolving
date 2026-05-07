# Function to calculate factorial
def factorial(num):
    result = 1

    # Check for negative number
    if num < 0:
        return "Factorial is not defined for negative numbers"

    # Calculate factorial
    for i in range(1, num + 1):
        result *= i

    return result


# Take input from the user
number = int(input("Enter a number: "))

# Call the function and print result
print("Factorial of", number, "is:", factorial(number))