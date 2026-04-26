# Take input from the user
N = int(input("Enter a number: "))

# Initialize sum
total = 0

# Loop from 1 to N
for i in range(1, N + 1):
    total += i

# Print the result
print("Sum from 1 to", N, "is:", total)