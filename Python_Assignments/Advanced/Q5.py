class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        # Add minutes and hours separately
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        total_minutes %= 60  # Keep minutes within 0-59

        # Return a new Time object with the result
        return Time(total_hours, total_minutes)

    def displayTime(self):
        # Display time in "hours and minutes" format
        print(f"{self.hours} hours and {self.minutes} minutes")

    def displayMinute(self):
        # Calculate and display total minutes in the Time object
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes}")


# Example usage:

# Initialize three Time objects
time1 = Time(1, 2)
time2 = Time(2, 45)
time3 = Time(1, 30)

# Display each time separately
print("Time 1:")
time1.displayTime()      # Output: "1 hours and 2 minutes"
time1.displayMinute()    # Output: "Total minutes: 62"

print("\nTime 2:")
time2.displayTime()      # Output: "2 hours and 45 minutes"
time2.displayMinute()    # Output: "Total minutes: 165"

print("\nTime 3:")
time3.displayTime()      # Output: "1 hours and 30 minutes"
time3.displayMinute()    # Output: "Total minutes: 90"

# Adding two time objects and displaying the result
print("\nResult of Time 2 + Time 3:")
result = time2.addTime(time3)
result.displayTime()      # Output: "4 hours and 15 minutes"
result.displayMinute()    # Output: "Total minutes: 255"
