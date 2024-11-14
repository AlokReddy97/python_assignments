def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return f"The file '{filename}' does not exist."

# Specify the filename
filename = "demo.txt"
line_count = count_lines(filename)
print(f"Number of lines in '{filename}': {line_count}")
