# Function to check prime number
def is_prime(num):
    # Prime numbers are greater than 1
    if num <= 1:
        return False

    # Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# Take input from the user
number = int(input("Enter a number: "))

# Call the function and display result
if is_prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is NOT a Prime Number")