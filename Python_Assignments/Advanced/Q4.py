class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0  # Default area for a generic shape

class Square(Shape):
    def __init__(self, length):
        super().__init__()  # Initialize the superclass
        self.length = length

    def area(self):
        return self.length * self.length  # Area of square = length^2

# Example usage:
square = Square(5)
print("Area of the square:", square.area())  # Should output 25

shape = Shape()
print("Area of the shape:", shape.area())  # Should output 0

