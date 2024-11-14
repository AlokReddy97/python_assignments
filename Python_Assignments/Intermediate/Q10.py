def generate_stone_piles(num_piles, start_stones):
    piles = []
    
    # Start from the specified number of stones, adding each pile with an increment of 2
    for i in range(num_piles):
        piles.append(start_stones)
        start_stones += 2
    
    return piles

# Take input for the number of piles and starting number of stones
num_piles = int(input("Enter the number of piles: "))
start_stones = int(input("Enter the starting number of stones in the first pile: "))

# Generate and print the list of stones in each pile
stones_in_piles = generate_stone_piles(num_piles, start_stones)
print("Number of stones in each pile:", stones_in_piles)
