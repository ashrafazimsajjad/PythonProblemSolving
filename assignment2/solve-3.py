# Function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    # Loop through each character
    for char in text:
        if char in vowels:
            count += 1

    return count


# Take input from the user
string = input("Enter a string: ")

# Call the function and print result
print("Number of vowels:", count_vowels(string))