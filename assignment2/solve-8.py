# Function to find the difference between two sets
def find_difference(set1, set2):
    return set1 - set2


# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Call the function and print result
result = find_difference(set1, set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Difference (Set1 - Set2):", result)