def calculate_grade():
    # Input marks for five subjects
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))
    biology = float(input("Enter Biology marks: "))
    mathematics = float(input("Enter Mathematics marks: "))
    computer = float(input("Enter Computer marks: "))

    # Calculate total marks and percentage
    total_marks = physics + chemistry + biology + mathematics + computer
    percentage = (total_marks / 500) * 100

    # Print the percentage
    print(f"Percentage: {percentage}%")

    # Assign grade based on percentage
    if percentage >= 90:
        print("Grade A")
    elif percentage >= 80:
        print("Grade B")
    elif percentage >= 70:
        print("Grade C")
    elif percentage >= 60:
        print("Grade D")
    elif percentage >= 40:
        print("Grade E")
    else:
        print("Grade F")

# Example usage
calculate_grade()
