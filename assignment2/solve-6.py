# Function to find common elements
def find_common_elements(list1, list2):
    common = []

    # Check each element in list1
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)

    return common


# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Call the function and print result
result = find_common_elements(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Common Elements:", result)