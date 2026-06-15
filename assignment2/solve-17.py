# Function to sort dictionary by values
def sort_dict_by_values(my_dict):
    # sorted() with key=lambda sorts based on values
    return dict(sorted(my_dict.items(), key=lambda item: item[1]))


# Example dictionary
my_dict = {"banana": 3, "apple": 5, "orange": 2, "mango": 4}

# Sort the dictionary
sorted_dict = sort_dict_by_values(my_dict)

# Print the result
print("Original Dictionary:", my_dict)
print("Dictionary Sorted by Values:", sorted_dict)