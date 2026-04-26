# Take input from the user
num = int(input("Enter a number: "))

# Nested if-else check
if num % 2 == 0:
    if num % 3 == 0:
        print("The number is divisible by both 2 and 3")
    else:
        print("The number is divisible by 2 but not by 3")
else:
    print("The number is not divisible by 2")