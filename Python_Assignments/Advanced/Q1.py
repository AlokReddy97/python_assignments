# Open the file in read mode
with open("doc.txt", "r") as file:
    # Read the content of the file
    content = file.read()

# Split content into words and filter only even-length words
even_length_words = [word for word in content.split() if len(word) % 2 == 0]

# Join the filtered words to maintain the original spacing
result = ' '.join(even_length_words)

# Print the result
print("Even length words from the file:")
print(result)
