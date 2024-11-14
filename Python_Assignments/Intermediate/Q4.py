# Function to rotate the array by D elements towards the right
def rotate_array(arr, D):
    N = len(arr)  # Get the size of the array
    
    # Normalize D to handle cases where D > N
    D = D % N
    
    # Perform the rotation using slicing
    rotated_arr = arr[-D:] + arr[:-D]
    
    return rotated_arr

# Take dynamic input for the array and D
arr = list(map(int, input("Enter the list of integers separated by spaces: ").split()))
D = int(input("Enter the number of elements to rotate the array by: "))

# Call the function to rotate the array
rotated_arr = rotate_array(arr, D)

# Print the rotated array
print("Array after rotation:", rotated_arr)
