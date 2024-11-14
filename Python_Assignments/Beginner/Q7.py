# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort both strings and compare them
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

# Taking user input for both strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the strings are anagrams and print the result
result = are_anagrams(string1, string2)
print(result)
