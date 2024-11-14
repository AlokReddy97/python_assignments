def count_vowels(input_string):
    # Define the set of vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    count = 0
    
    # Loop through each character in the string and check if it's a vowel
    for char in input_string:
        if char in vowels:
            count += 1
    
    return count

# Take dynamic input from the user
input_string = input("Enter a string: ")

# Call the function and print the result
vowel_count = count_vowels(input_string)
print(f"Number of vowels: {vowel_count}")
