# Function to find the length of a list
def find_length(my_list):
    count = 0

    # Count each element in the list
    for item in my_list:
        count += 1

    return count


# Example list
numbers = [10, 20, 30, 40, 50]

# Call the function and print result
print("Length of the list is:", find_length(numbers))