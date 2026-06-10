# Function to convert a list into a set
def list_to_set(my_list):
    return set(my_list)


# Example list
numbers = [1, 2, 3, 4, 5, 2, 3, 4]

# Call the function and print result
result = list_to_set(numbers)

print("Original List:", numbers)
print("Converted Set:", result)