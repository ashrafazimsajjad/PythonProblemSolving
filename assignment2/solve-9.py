# Function to check if set1 is a subset of set2
def is_subset(set1, set2):
    return set1.issubset(set2)


# Example sets
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Call the function and print result
if is_subset(set1, set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is NOT a subset of Set2")