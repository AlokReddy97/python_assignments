# Function to find common elements between two lists
def find_common_elements(l1, l2):
    # Using set intersection to find common elements
    common_elements = list(set(l1) & set(l2))
    return common_elements

# Taking input for both lists
l1 = input("Enter elements of the first list (separate by space): ").split()
l2 = input("Enter elements of the second list (separate by space): ").split()

# Convert input strings to integers
l1 = [int(i) for i in l1]
l2 = [int(i) for i in l2]

# Find and print the common elements
common_elements = find_common_elements(l1, l2)
print("Common elements:", common_elements)
