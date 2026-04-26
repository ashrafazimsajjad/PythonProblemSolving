# Take input from the user
grade = input("Enter grade (A/B/C): ").upper()

# Use match-case
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Invalid grade")