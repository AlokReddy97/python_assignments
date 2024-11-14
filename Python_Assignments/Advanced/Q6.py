# Base class for Single and Multilevel Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

# Derived class inheriting from Animal (Single Inheritance)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Another base class for Multiple Inheritance
class Runner:
    def __init__(self, speed):
        self.speed = speed

    def run(self):
        return f"Running at {self.speed} km/h"

# Derived class inheriting from both Animal and Runner (Multiple Inheritance)
class Greyhound(Animal, Runner):
    def __init__(self, name, speed):
        Animal.__init__(self, name)
        Runner.__init__(self, speed)

# Derived class inheriting from Dog (Multilevel Inheritance)
class GuideDog(Dog):
    def guide(self):
        return f"{self.name} is guiding the way."


# Creating instances to demonstrate each inheritance type

# Single Inheritance
dog = Dog("Buddy")
print("Single Inheritance:")
print(dog.speak())  # Output: "Buddy says Woof!"
print()

# Multiple Inheritance
greyhound = Greyhound("Flash", 45)
print("Multiple Inheritance:")
print(greyhound.speak())  # Output: "Flash says Woof!"
print(greyhound.run())    # Output: "Running at 45 km/h"
print()

# Multilevel Inheritance
guide_dog = GuideDog("Max")
print("Multilevel Inheritance:")
print(guide_dog.speak())  # Output: "Max says Woof!"
print(guide_dog.guide())  # Output: "Max is guiding the way."
