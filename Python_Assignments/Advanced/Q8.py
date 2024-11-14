def parse_encoded_string(encoded_string):
    # Split the string by '0'
    parts = encoded_string.split('0')
    print(parts)
    # Remove any empty strings that might have been created due to leading, trailing, or consecutive zeros
    parts = [part for part in parts if part]

    # Check if the parts have the expected number of elements (first name, last name, and id)
    if len(parts) == 3:
        # Create a dictionary to store the first name, last name, and id
        result = {
            "first_name": parts[0],
            "last_name": parts[1],
            "id": parts[2]
        }
        return result
    else:
        # If there aren't exactly 3 parts, return an error or handle accordingly
        return "Invalid input format"

# Input: Dynamically entered string
encoded_string = input("Enter the encoded string: ")

# Call the function and display the result
result = parse_encoded_string(encoded_string)
print(result)
