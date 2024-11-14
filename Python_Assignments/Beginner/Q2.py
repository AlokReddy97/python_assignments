def count_alphabets_and_numbers(input_string):
    alphabets = 0
    numbers = 0
    for char in input_string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            numbers += 1
    print(f"Alphabets: {alphabets} & Number: {numbers}")

# Example usage
input_string = input("Enter a string: ")
count_alphabets_and_numbers(input_string)
