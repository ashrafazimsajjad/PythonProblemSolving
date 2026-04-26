# Display menu
print("Menu:")
print("1 → Add")
print("2 → Subtract")
print("3 → Exit")

# Take user choice
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        # Addition
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)

    case 2:
        # Subtraction
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)

    case 3:
        # Exit
        print("Exiting program...")

    case _:
        print("Invalid choice! Please select 1, 2, or 3.")