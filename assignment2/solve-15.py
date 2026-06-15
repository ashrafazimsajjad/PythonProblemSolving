# Function to merge two dictionaries
def merge_dicts(dict1, dict2):
    # Method 1: Using dictionary unpacking (Python 3.5+)
    merged = {**dict1, **dict2}
    return merged

# Example dictionaries
dict1 = {"name": "Sajjad", "age": 25}
dict2 = {"city": "Dhaka", "country": "Bangladesh"}

# Merge dictionaries
merged_dict = merge_dicts(dict1, dict2)

# Print the merged dictionary
print("Merged Dictionary:", merged_dict)


#Alternative Method Using update():
dict1 = {"name": "Sajjad", "age": 25}
dict2 = {"city": "Dhaka", "country": "Bangladesh"}

# Merge dict2 into dict1
dict1.update(dict2)

print("Merged Dictionary:", dict1)