# Function to return a new list with unique elements
def unique_elements(input_list):
    # Convert the list to a set to remove duplicates, then back to a list
    return list(set(input_list))

# Take input dynamically from the user
input_list = input("Enter a list of elements separated by spaces: ").split()

# Convert the input elements to integers (assuming the input list should contain integers)
input_list = [int(i) for i in input_list]

# Get the list with unique elements
list2 = unique_elements(input_list)

# Output the result
print("List with unique elements:", list2)
