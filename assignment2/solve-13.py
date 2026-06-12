# Function to create a dictionary from two lists
def create_dictionary(keys, values):
    return dict(zip(keys, values))


# Example lists
keys = ["name", "age", "city"]
values = ["Sajjad", 25, "Dhaka"]

# Create dictionary
my_dict = create_dictionary(keys, values)

# Print the dictionary
print("Dictionary:", my_dict)

#Alternative Without a Function:

# Two lists
keys = ["name", "age", "city"]
values = ["Sajjad", 25, "Dhaka"]

# Create dictionary
my_dict = dict(zip(keys, values))

print(my_dict)