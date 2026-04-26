# Take marks input from the user
marks = float(input("Enter student's marks: "))

# Check grade using if-elif-else
if marks >= 90:
    print("Grade: A")
elif 75 <= marks <= 89:
    print("Grade: B")
elif 50 <= marks <= 74:
    print("Grade: C")
else:
    print("Grade: Fail")