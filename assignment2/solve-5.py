# Function to remove even numbers from a list
def remove_even_numbers(numbers):
    odd_numbers = []

    # Keep only odd numbers
    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)

    return odd_numbers


# Example list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Call the function and print result
result = remove_even_numbers(numbers)

print("Original List:", numbers)
print("List after removing even numbers:", result)