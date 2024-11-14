# Function to find and return pairs whose sum is equal to K
def find_pairs(arr, k):
    pairs = []  # To store the pairs
    seen = set()  # To track the numbers we've already seen

    # Traverse through the array
    for num in arr:
        complement = k - num  # Find the complement

        # If the complement exists in the seen set, it's a valid pair
        if complement in seen:
            pairs.append((num, complement))
        
        # Add the current number to the seen set
        seen.add(num)
    
    return pairs

# Take dynamic input from the user for the array and the value of K
arr = list(map(int, input("Enter the list of integers separated by spaces: ").split()))
k = int(input("Enter the value of K: "))

# Call the function and get the pairs
pairs = find_pairs(arr, k)

# Print the results
if pairs:
    print("Pairs whose sum is equal to", k, "are:", pairs)
    print("Pair count:", len(pairs))
else:
    print("No pairs found with the sum equal to", k)
