# Take input from the user
user_input = input("Enter something: ")

# Try to detect the correct data type
try:
    # Check for integer
    value = int(user_input)
    print("Data type is:", type(value))
except ValueError:
    try:
        # Check for float
        value = float(user_input)
        print("Data type is:", type(value))
    except ValueError:
        # Check for boolean
        if user_input.lower() == "true":
            print("Data type is:", type(True))
        elif user_input.lower() == "false":
            print("Data type is:", type(False))
        else:
            # Otherwise, it is a string
            print("Data type is:", type(user_input))