# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division and modulus safely (avoid division by zero)
if num2 != 0:
    division = num1 / num2
    modulus = num1 % num2
else:
    division = "Undefined (division by zero)"
    modulus = "Undefined (modulus by zero)"

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)