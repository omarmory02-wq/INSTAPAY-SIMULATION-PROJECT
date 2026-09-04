# InstaPay Simulation 💳

A simple **InstaPay payment system simulation built with Python**.
This project demonstrates the basic functionality of a digital payment application, including user registration, authentication, card linking, deposits, withdrawals, money transfers, and transaction history.

The project is designed as a **console-based application** and focuses on applying Python programming concepts such as functions, dictionaries, loops, conditional statements, input validation, and modular programming.

---

## 📌 Project Overview

The InstaPay Simulation allows users to create an account and securely interact with their virtual payment account.

After logging in, users can:

* 💰 View their current balance
* 💳 Link a Visa card
* ➕ Deposit money
* ➖ Withdraw money
* 🔄 Transfer money to another user
* 📜 View transaction history
* 🚪 Log out of their account

The application starts with a main menu where users can choose to register, log in, or exit.

---

## ✨ Features

### 👤 User Registration

Users can create a new account by providing:

* Username
* Full name
* Phone number
* Password

The system checks that the username is unique and validates the entered information before creating the account. Each new account starts with a balance of **0 EGP**.

### 🔐 Login System

Users can log in using their username and password.

The system allows up to **3 login attempts** before returning the user to the main menu.

### 💳 Card Linking

Users can link a Visa card by entering:

* Cardholder name
* 16-digit card number
* Expiry date
* 3-digit CVV

For the stored card information, the card number is masked so that only the last four digits are displayed, and the CVV is not stored.

### 💰 Deposit

Users can deposit money into their account.

The system checks that the entered amount is valid and greater than zero, then updates the user's balance and records the deposit in the transaction history.

### 💸 Withdrawal

Users can withdraw money from their balance.

The system checks that:

* The amount is valid
* The amount is greater than zero
* The user has sufficient balance

The withdrawal is then recorded in the transaction history.

### 🔄 Money Transfer

Users can transfer money to another registered user.

The application checks that:

* The recipient exists
* The sender is not transferring to themselves
* The transfer amount is valid
* The sender has sufficient balance

The transfer must also be confirmed before the money is moved. Both the sender and recipient receive a transaction record.

### 📜 Transaction History

Users can view their previous transactions, including:

* Deposits
* Withdrawals
* Transfers In
* Transfers Out

If no transactions exist, the application displays an appropriate message.

---

## 🗂️ Project Structure

```text
InstaPay-Simulation/
│
├── main.py
├── auth.py
├── operations.py
├── validation.py
└── README.md
```

### `main.py`

Controls the main application flow and menus.

It provides the main InstaPay menu and the logged-in user's menu, connecting authentication with the available payment operations.

### `auth.py`

Handles user authentication functionality:

* User registration
* User login
* Finding users
* Storing user account information

The application's users are stored in a Python dictionary.

### `operations.py`

Contains the main financial operations:

* View balance
* Link card
* Deposit
* Withdraw
* Transfer
* View transaction history

### `validation.py`

Contains validation functions for:

* Username
* Password
* Phone number
* Amount
* Card number
* CVV

For example, usernames cannot contain spaces, passwords must contain at least six characters, and phone numbers must be 11 digits starting with `01`.

---

## 🛠️ Technologies Used

* **Python 3**
* Python Dictionaries
* Functions
* Loops
* Conditional Statements
* Input Validation
* Modular Programming

No external libraries are required to run the project.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/instapay-simulation.git
```

### 2. Open the project folder

```bash
cd instapay-simulation
```

### 3. Run the application

```bash
python main.py
```

---

## 🧭 How to Use

When the application starts, you will see:

```text
===== InstaPay =====
1. Register
2. Login
3. Exit
```

### Register

Choose `1` and create a new account.

### Login

Choose `2` and enter your username and password.

After a successful login, the following menu becomes available:

```text
===== Main Menu =====
1. View Balance
2. Link Card
3. Deposit
4. Withdraw
5. Transfer
6. Transaction History
7. Logout
```

Choose the operation you want to perform.

---

## 🔒 Validation & Security Considerations

The project includes basic validation to prevent invalid user input.

Examples include:

* Duplicate usernames are rejected.
* Passwords must contain at least 6 characters.
* Phone numbers must follow the required 11-digit format.
* Card numbers must contain 16 digits.
* CVVs must contain 3 digits.
* Deposits and withdrawals must be greater than zero.
* Withdrawals and transfers cannot exceed the available balance.
* Users cannot transfer money to themselves.

The linked card number is displayed in masked form, and the CVV is not stored in the user data structure.

> **Note:** This is an educational simulation and should not be used for handling real financial transactions or real payment-card information.

---

## 🎯 Learning Objectives

This project demonstrates practical use of Python programming concepts, including:

1. **Functions** – organizing the application into reusable operations.
2. **Dictionaries** – storing users, account information, and transactions.
3. **Loops** – creating interactive menus and handling repeated input.
4. **Conditional Statements** – validating input and controlling application logic.
5. **Input Validation** – preventing invalid data from being accepted.
6. **Modular Programming** – separating authentication, validation, operations, and the main application into different files.
7. **Data Management** – updating balances and maintaining transaction records.

---

## 🚀 Possible Future Improvements

Some improvements that could be added in future versions include:

* Password hashing instead of storing passwords directly.
* Persistent database storage such as SQLite or MySQL.
* More advanced card validation.
* Transaction timestamps.
* Transaction IDs.
* Transfer receipts.
* Improved user interface.
* Admin functionality.
* Better error handling.
* Account deletion and password change functionality.
* A graphical user interface (GUI).

---

## 👨‍💻 Project Type

**Educational Python Project – InstaPay Simulation**

This project was developed to practice Python programming, modular application design, authentication, validation, and basic financial transaction logic.

---

## ⚠️ Disclaimer

This project is **only a simulation for educational purposes**. It is not affiliated with or connected to the official InstaPay service and should not be used with real banking information, payment cards, or financial transactions.

