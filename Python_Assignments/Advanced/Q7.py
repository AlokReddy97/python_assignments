# Input: Taking student names and subjects dynamically
students = input("Enter student names separated by a comma: ").split(",")
subjects = input("Enter subjects corresponding to the students separated by a comma: ").split(",")

# Stripping any leading/trailing spaces
students = [student.strip() for student in students]
subjects = [subject.strip() for subject in subjects]

# Check if both lists have the same length and construct the dictionary using list comprehension
student_subject_dict = {students[i]: subjects[i] for i in range(len(students))} if len(students) == len(subjects) else {}

# Output: Dictionary using list comprehension
if student_subject_dict:
    print("Dictionary using list comprehension:")
    print(student_subject_dict)
else:
    print("Error: The number of students and subjects must be the same!")
