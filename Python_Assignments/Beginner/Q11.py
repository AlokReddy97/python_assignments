# Function to calculate sum of digits of a number
def sum_of_digits(num):
    # Sum the digits of the number until it's a single digit
    while num >= 10:
        num = sum(int(digit) for digit in str(num))  # Sum digits of the number
    return num

# Take input from the user
num = int(input("Enter a number: "))

# First sum of digits
first_sum = sum(int(digit) for digit in str(num))
print(f"Sum_of_digits = {first_sum}")

# Now reduce to a single-digit sum
final_result = sum_of_digits(first_sum)
print(f"Final Output: {final_result}")
