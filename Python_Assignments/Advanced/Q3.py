def JtoI(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        # Replace all occurrences of 'J' with 'I'
        corrected_content = content.replace('J', 'I')
        
        print("Corrected Content:\n")
        print(corrected_content)
    
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")

# Specify the filename
filename = "words.txt"
JtoI(filename)
