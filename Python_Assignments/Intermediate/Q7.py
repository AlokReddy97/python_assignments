def find_median(numbers):
    # Sort the list first
    numbers.sort()
    
    # Get the length of the list
    n = len(numbers)
    
    # If the list has an odd length, return the middle element
    if n % 2 != 0:
        median = numbers[n // 2]
    else:
        # If the list has an even length, return the average of the two middle elements
        median = (numbers[(n // 2) - 1] + numbers[n // 2]) / 2
    
    return median

# Input: Take a list of numbers dynamically from the user
number_list = list(map(int, input("Enter a list of numbers (space-separated): ").split()))

# Find and print the median
median = find_median(number_list)
print(f"Median: {median}")

