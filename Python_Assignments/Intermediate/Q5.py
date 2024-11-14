# Function to analyze weather data
def analyze_weather_data(temperature_readings):
    # Calculate the average, highest, and lowest temperatures
    avg_temperature = sum(temperature_readings) / len(temperature_readings)
    highest_temperature = max(temperature_readings)
    lowest_temperature = min(temperature_readings)
    
    # Return the results as a tuple
    return avg_temperature, highest_temperature, lowest_temperature

# Take dynamic input for temperature readings
temperature_readings = list(map(int, input("Enter the list of temperature readings separated by spaces: ").split()))

# Call the function to analyze the data
avg_temperature, highest_temperature, lowest_temperature = analyze_weather_data(temperature_readings)

# Print the results
print(f"Average Temperature: {avg_temperature:.1f}")
print(f"Highest Temperature: {highest_temperature}")
print(f"Lowest Temperature: {lowest_temperature}")

