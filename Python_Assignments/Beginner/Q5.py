# Function to calculate factorial using for loop
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# Input from user
num = int(input("Enter a number to find its factorial: "))

# Calculate and print the factorial
print(f"The factorial of {num} is: {factorial(num)}")
