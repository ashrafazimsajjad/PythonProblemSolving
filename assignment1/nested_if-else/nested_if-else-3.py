# Predefined username and password
valid_username = "admin"
valid_password = "1234"

# Take input from the user
username = input("Enter username: ")
password = input("Enter password: ")

# Nested if-else for login check
if username == valid_username:
    if password == valid_password:
        print("Login Successful")
    else:
        print("Check Password")
else:
    print("Invalid user")