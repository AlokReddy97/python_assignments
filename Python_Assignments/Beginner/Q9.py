def get_input():
    input_list = []
    while True:
        try:
            # Ask user to input a number
            user_input = input("Enter a number (or type 'done' to finish): ")
            
            # Allow the user to finish input by typing 'done'
            if user_input.lower() == 'done':
                break
            
            # Try converting the input to an integer
            num = int(user_input)
            
            # Append the valid integer to the list
            input_list.append(num)
        
        except ValueError:
            # If the input cannot be converted to an integer, print an error message
            print("Error: Please enter a valid integer.")
    
    return input_list

# Main part of the program
input_list = get_input()
print(f"Entered List: {input_list}")

# Now we can count the frequency of elements in the list
frequency_count = {}
for num in input_list:
    frequency_count[num] = frequency_count.get(num, 0) + 1

print("Frequency count:", frequency_count)
