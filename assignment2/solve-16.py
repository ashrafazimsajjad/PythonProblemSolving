# Function to sort dictionary by keys
def sort_dict_by_keys(my_dict):
    # Returns a new dictionary sorted by keys
    return dict(sorted(my_dict.items()))


# Example dictionary
my_dict = {"banana": 3, "apple": 5, "orange": 2, "mango": 4}

# Sort the dictionary
sorted_dict = sort_dict_by_keys(my_dict)

# Print the result
print("Original Dictionary:", my_dict)
print("Dictionary Sorted by Keys:", sorted_dict)