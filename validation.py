def validate_username(username, users):
    if not username or " " in username:
        return False, "Username cannot be empty or contain spaces."
    if username in users:
        return False, "Username already exists."
    return True, ""

def validate_password(password):
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."
    return True, ""

def validate_phone(phone):
    if not phone.isdigit() or len(phone) != 11 or not phone.startswith("01"):
        return False, "Phone number must be an 11-digit number starting with '01'."
    return True, ""

def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        if amount <= 0:
            return False, "Amount must be greater than 0.", 0.0
        return True, "", amount
    except ValueError:
        return False, "Invalid amount. Please enter a valid number.", 0.0

def validate_card_number(card_number):
    if not card_number.isdigit() or len(card_number) != 16:
        return False, "Card number must be 16 digits."
    return True, ""

def validate_cvv(cvv):
    if not cvv.isdigit() or len(cvv) != 3:
        return False, "CVV must be 3 digits."
    return True, ""