# Function to check if a number is perfect
def is_perfect_number(num):
    # Initialize sum of divisors
    sum_of_divisors = 0
    
    # Find divisors and calculate the sum
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    
    # Check if the sum of divisors is equal to the number
    if sum_of_divisors == num:
        return "Yes"
    else:
        return "No"

# Input from user
num = int(input("Enter a number to check if it's a perfect number: "))

# Check if the number is perfect and print the result
result = is_perfect_number(num)
print(result)
