def count_walked_away_customers(N, S):
    computers_available = N
    waiting_customers = set()
    customers_in_cafe = set()

    for customer in S:
        if customer in customers_in_cafe:
            # Customer is leaving, so free the computer
            customers_in_cafe.remove(customer)
            computers_available += 1
        else:
            # Customer is arriving
            if computers_available > 0:
                # Allocate a computer to the arriving customer
                customers_in_cafe.add(customer)
                computers_available -= 1
            else:
                # No computer available, customer walks away
                waiting_customers.add(customer)
    
    return len(waiting_customers)

# Test cases
N1 = 3
S1 = "GACCBDDBAGEE"
print(count_walked_away_customers(N1, S1))  # Output: 1

N2 = 1
S2 = "ABCBAC"
print(count_walked_away_customers(N2, S2))  # Output: 2
