import getpass
from tabulate import tabulate

# Empty list to store user data
users = []

def sign_up():
    name = input("Enter your name: ")
    email = input("Enter your email ID: ")
    password = getpass.getpass("Enter your password: ")
    
    # To check if email already exists
    for user in users:
        if user['Email'] == email:
            print("Email already registered. Try logging in.")
            return
    
    user_data = {"Name": name, "Email": email, "Password": password}
    users.append(user_data)
    print("Sign-up successful!")

def login():
    email = input("Enter your email ID: ")
    password = getpass.getpass("Enter your password: ")
    
    for user in users:
        if user['Email'] == email and user['Password'] == password:
            print("Login successful!")
            return
    print("Login failed! Incorrect email or password.")

def delete_user():
    email = input("Enter the email ID of the user to delete: ")
    for user in users:
        if user['Email'] == email:
            users.remove(user)
            print("User deleted successfully!")
            return
    print("User not found!")

def display_users():
    if not users:
        print("No users registered.")
        return
    print("\nRegistered Users:")
    print(tabulate(users, headers="keys", tablefmt="pretty"))

while True:
    print("\n1. Sign Up\n2. Login\n3. Delete User\n4. Display Users\n5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        sign_up()
    elif choice == '2':
        login()
    elif choice == '3':
        delete_user()
    elif choice == '4':
        display_users()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
