# Function to reverse the order of words in a sentence
def reverse_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list of words back into a string
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Take input from the user
input_sentence = input("Enter a sentence: ")

# Call the function and print the reversed sentence
output_sentence = reverse_sentence(input_sentence)
print("Output after reverse =", output_sentence)
