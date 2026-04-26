# Take input from the user
year = int(input("Enter a year: "))

# Check leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a Leap Year")
else:
    print("It is NOT a Leap Year")