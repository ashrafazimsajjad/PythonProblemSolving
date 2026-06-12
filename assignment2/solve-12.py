# Function to find maximum and minimum values
def find_max_min(my_tuple):
    return max(my_tuple), min(my_tuple)

# Example tuple
numbers = (10, 25, 5, 40, 15)

# Call the function
maximum, minimum = find_max_min(numbers)

print("Maximum value:", maximum)
print("Minimum value:", minimum)