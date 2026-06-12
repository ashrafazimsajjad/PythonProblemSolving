# Function to count character frequency
def char_frequency(text):
    freq = {}  # Create an empty dictionary

    for char in text:
        if char in freq:
            freq[char] += 1  # Increment count if char exists
        else:
            freq[char] = 1   # Initialize count to 1 if char is new

    return freq


# Take input from the user
string = input("Enter a string: ")

# Call the function and print result
frequency = char_frequency(string)

print("Character Frequency:")
for char, count in frequency.items():
    print(f"'{char}': {count}")