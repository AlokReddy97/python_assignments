# Function to calculate the LCM of two numbers
def lcm(a, b):
    # Calculate the Greatest Common Divisor (GCD) using the math.gcd function
    import math
    return abs(a * b) // math.gcd(a, b)

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the LCM and print the result
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")
