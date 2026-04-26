# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Shorthand if-else to find maximum
maximum = num1 if num1 > num2 else num2

# Print the result
print("The maximum number is:", maximum)