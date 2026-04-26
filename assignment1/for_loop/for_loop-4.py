# Take input from the user
text = input("Enter a string: ")

# Initialize counter
count = 0

# Define vowels
vowels = "aeiouAEIOU"

# Loop through each character
for char in text:
    if char in vowels:
        count += 1

# Print the result
print("Number of vowels:", count)