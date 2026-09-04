from auth import users

def show_balance(username):
    # Get the balance directly from the dictionary
    balance = users[username]["balance"]
    print(f"Current Balance: {balance} EGP")

def link_card(username):
    print("\n--- Link Visa Card ---")
    card_holder = input("Enter cardholder name: ")
    card_number = input("Enter 16-digit card number: ")
    expiry = input("Enter expiry date: ")
    cvv = input("Enter CVV: ")

    # Check length for card number and CVV
    if len(card_number) != 16 or not card_number.isdigit():
        print("Error: Card number must be 16 digits.")
        return

    if len(cvv) != 3 or not cvv.isdigit():
        print("Error: CVV must be 3 digits.")
        return

    # Save card info safely without storing the CVV
    users[username]["card"] = {
        "holder": card_holder,
        "number": "**** " + card_number[-4:],
        "expiry": expiry
    }
    print("Card linked successfully!")

def deposit(username):
    print("\n--- Deposit ---")
    amount_input = input("Enter amount: ")

    # Convert user input to integer
    if not amount_input.isdigit():
        print("Error: Please enter a positive number.")
        return

    amount = int(amount_input)
    if amount <= 0:
        print("Error: Amount must be greater than 0.")
        return

    # Update balance and record transaction
    users[username]["balance"] = users[username]["balance"] + amount
    
    users[username]["transactions"].append({
        "type": "Deposit",
        "amount": amount
    })
    
    print(f"Deposit successful! New Balance: {users[username]['balance']} EGP")

def withdraw(username):
    print("\n--- Withdraw ---")
    amount_input = input("Enter amount: ")

    if not amount_input.isdigit():
        print("Error: Please enter a positive number.")
        return

    amount = int(amount_input)
    if amount <= 0:
        print("Error: Amount must be greater than 0.")
        return

    # Check if the user has enough money
    current_balance = users[username]["balance"]
    if amount > current_balance:
        print("Error: Insufficient balance.")
        return

    # Deduct balance and record transaction
    users[username]["balance"] = current_balance - amount
    
    users[username]["transactions"].append({
        "type": "Withdraw",
        "amount": amount
    })
    
    print(f"Withdrawal successful! Remaining Balance: {users[username]['balance']} EGP")

def transfer(username):
    print("\n--- Transfer Money ---")
    recipient = input("Recipient username: ")

    # Basic checks for recipient
    if recipient not in users:
        print("Error: Recipient does not exist.")
        return

    if recipient == username:
        print("Error: You cannot transfer money to yourself.")
        return

    amount_input = input("Amount: ")
    if not amount_input.isdigit():
        print("Error: Please enter a positive number.")
        return

    amount = int(amount_input)
    if amount <= 0:
        print("Error: Amount must be greater than 0.")
        return

    # Check balance
    sender_balance = users[username]["balance"]
    if amount > sender_balance:
        print("Error: Insufficient balance.")
        return

    confirm = input("Confirm transfer? (yes/no): ")
    if confirm.lower() == "yes":
        # Transfer money between dictionary accounts
        users[username]["balance"] = sender_balance - amount
        users[recipient]["balance"] = users[recipient]["balance"] + amount

        # Save history for sender
        users[username]["transactions"].append({
            "type": "Transfer Out",
            "amount": amount
        })
        
        # Save history for recipient
        users[recipient]["transactions"].append({
            "type": "Transfer In",
            "amount": amount
        })

        print(f"Transfer successful! Your new balance: {users[username]['balance']} EGP")
    else:
        print("Transfer cancelled.")

def show_transactions(username):
    print("\n===== Transaction History =====")
    history = users[username]["transactions"]

    if len(history) == 0:
        print("No transactions found.")
        return

    # Loop through each saved transaction dictionary
    for t in history:
        print(f"Type: {t['type']} | Amount: {t['amount']} EGP")