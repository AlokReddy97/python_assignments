# Function to reverse a number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        # Extract the last digit
        last_digit = num % 10
        # Build the reversed number
        reversed_num = reversed_num * 10 + last_digit
        # Remove the last digit from the original number
        num = num // 10
    return reversed_num

# Take input from the user
num = int(input("Enter a number: "))

# Call the function and display the reversed number
reversed_num = reverse_number(num)
print(f"Reversed Number: {reversed_num}")
