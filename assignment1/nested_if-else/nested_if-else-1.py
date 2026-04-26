# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Nested if-else to find the largest number
if num1 > num2:
    if num1 > num3:
        print("First number is the largest number:", num1)
    else:
        print("Third number is the largest number:", num3)
else:
    if num2 > num3:
        print("Second number is the largest number:", num2)
    else:
        print("Third number is the largest number::", num3)