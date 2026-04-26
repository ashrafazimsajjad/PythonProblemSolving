# Take input from the user
age = int(input("Enter your age: "))

# Nested if-else for ticket pricing
if age < 5:
    print("Ticket Price: Free")
else:
    if age <= 18:
        print("Ticket Price: Discount")
    else:
        print("Ticket Price: Full price")