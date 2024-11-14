def login():
    # Pre-defined credentials (these can be customized or stored securely)
    correct_username = "user123"
    correct_password = "password123"

    # Ask for username input
    username = input("Enter username: ")

    # Check if the entered username is correct
    if username == correct_username:
        attempts = 0  # Count the number of password attempts

        while attempts < 3:
            # Ask for password and re-type password
            password = input("Enter password: ")


            # Verify if the password matches the pre-defined correct password
            if password == correct_password:
                print("Login successful!")
                return  # Exit the function on successful login
            else:
                print("Incorrect password. Try again.")
                attempts += 1

        # If attempts reach 3, display a message and exit
        print("Maximum attempts reached. Login failed.")
    else:
        print("Invalid username.")

# Call the login function
login()
