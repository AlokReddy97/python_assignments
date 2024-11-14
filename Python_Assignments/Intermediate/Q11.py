# Take input of words in a list dynamically from the user
input_strings = input("Enter a list of words separated by commas: ").split(",")

# Use map function to convert each string to a list of characters
# We strip each item to remove any extra spaces around words
output = list(map(lambda word: list(word.strip()), input_strings))

# Print the output list of lists
print("Output:", output)

