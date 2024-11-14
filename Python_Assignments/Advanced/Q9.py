def run_length_encode(a):
    final_string = ""  # Initialize an empty string for the result
    count = 1  # Initial count for the first character
    
    # Loop from index 0 to n-2 to handle the pair (a[i], a[i+1])
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:  # Check if the current character is the same as the next one
            count += 1  # Increment the count for consecutive characters
        else:
            final_string += a[i] + str(count)  # Append the character and its count to the final string
            count = 1  # Reset count for the next character

    # Append the last character and its count after the loop ends
    final_string += a[-1] + str(count)
    
    return final_string

# Dynamically take input
input_string = input("Enter a string: ")

# Get the encoded result
encoded_string = run_length_encode(input_string)
print(f"Run-length encoded string: {encoded_string}")
