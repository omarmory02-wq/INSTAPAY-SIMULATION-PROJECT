from auth import register, login
from operations import (
    show_balance,
    link_card,
    deposit,
    withdraw,
    transfer,
    show_transactions
)

def user_menu(current_user):
    while True:
        print("\n===== Main Menu =====")
        print("1. View Balance")
        print("2. Link Card")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Transaction History")
        print("7. Logout")

        choice = input("Choose: ").strip()

        if choice == "1":
            show_balance(current_user)
        elif choice == "2":
            link_card(current_user)
        elif choice == "3":
            deposit(current_user)
        elif choice == "4":
            withdraw(current_user)
        elif choice == "5":
            transfer(current_user)
        elif choice == "6":
            show_transactions(current_user)
        elif choice == "7":
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

def main():
    while True:
        print("\n===== InstaPay =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            logged_in_user = login()
            if logged_in_user:
                user_menu(logged_in_user)
        elif choice == "3":
            print("Thank you for using InstaPay simulation. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()