def access_element_at_index(lst, index):
    try:
        # Attempt to access the element at the specified index
        element = lst[index]
        print(f"Element at index {index} is: {element}")
    except IndexError:
        # Handle the IndexError if the index is out of range
        print(f"Error: Index {index} is out of range for the list.")

# Take input for list elements
input_list = []
num_elements = int(input("Enter the number of elements in the list: "))
print("Enter the elements of the list:")
for _ in range(num_elements):
    element = input()
    input_list.append(element)

# Take input for index
index_to_access = int(input("Enter the index you want to access: "))

# Call the function to access the element at the given index
access_element_at_index(input_list, index_to_access)
