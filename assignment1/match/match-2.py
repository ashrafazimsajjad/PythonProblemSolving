# Take input from the user
day = int(input("Enter a number (1-7): "))

# Use match-case
match day:
    case 1:
        print("Saturday")
    case 2:
        print("Sunday")
    case 3:
        print("Monday")
    case 4:
        print("Tuesday")
    case 5:
        print("Wednesday")
    case 6:
        print("Thursday")
    case 7:
        print("Friday")
    case _:
        print("Invalid input! Please enter a number between 1 and 7.")