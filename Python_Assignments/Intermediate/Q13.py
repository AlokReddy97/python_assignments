# Input the string and character dynamically
input_string = input("Enter a string: ")
given_char = input("Enter the character to check: ")

# Lambda function to check if the string starts with the given character
starts_with_char = lambda s, c: s.startswith(c)

# Check and print the result
result = starts_with_char(input_string, given_char)
print("Output:", result)
