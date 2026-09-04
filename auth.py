from validation import validate_username, validate_password, validate_phone

# Central data structure storing users
users = {}

def find_user(username):
    return users.get(username)

def register():
    print("\n--- Register ---")
    while True:
        username = input("Enter username: ").strip()
        is_valid, msg = validate_username(username, users)
        if is_valid:
            break
        print(f"Error: {msg}")

    name = input("Enter full name: ").strip()

    while True:
        phone = input("Enter phone number: ").strip()
        is_valid, msg = validate_phone(phone)
        if is_valid:
            break
        print(f"Error: {msg}")

    while True:
        password = input("Enter password: ").strip()
        is_valid, msg = validate_password(password)
        if is_valid:
            break
        print(f"Error: {msg}")

    users[username] = {
        "name": name,
        "phone": phone,
        "password": password,
        "balance": 0.0,
        "card": None,
        "transactions": []
    }
    print("Registration successful!")

def login():
    print("\n--- Login ---")
    attempts = 3
    while attempts > 0:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        user = find_user(username)
        if user and user["password"] == password:
            print(f"\nLogin successful! Welcome {user['name']}")
            return username

        attempts -= 1
        print(f"Invalid username or password. Remaining attempts: {attempts}")

    print("Login failed. Returning to main menu.")
    return None