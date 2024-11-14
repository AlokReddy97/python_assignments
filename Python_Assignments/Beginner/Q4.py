def sum_of_odd_numbers(start, stop):
    odd_sum = 0
    for number in range(start, stop + 1):
        if number % 2 != 0:
            odd_sum += number
    print(f"Sum of odd numbers between {start} and {stop}: {odd_sum}")

# Example usage
start = int(input("Enter start number: "))
stop = int(input("Enter stop number: "))
sum_of_odd_numbers(start, stop)
