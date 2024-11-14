# Recursive function to check if a number is a power of two
def is_power_of_two(n):
    # Base cases
    if n <= 0:
        return False
    if n == 1:
        return True
    # Recursive case: divide by 2 and check again
    if n % 2 == 0:
        return is_power_of_two(n // 2)
    else:
        return False

# Input: Take a number as input from the user
num = int(input("Enter a number: "))

# Check if the number is a power of two
if is_power_of_two(num):
    print(f"{num} is a power of two.")
else:
    print(f"{num} is not a power of two.")
