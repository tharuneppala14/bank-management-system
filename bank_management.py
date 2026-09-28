import json
import os

FILE_NAME = "accounts.json"


def load_accounts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


def create_account(accounts):
    account_no = input("Enter account number: ")

    if account_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter account holder name: ")
    phone = input("Enter phone number: ")

    try:
        initial_deposit = float(input("Enter initial deposit: "))

        if initial_deposit < 0:
            print("Deposit cannot be negative.")
            return

    except ValueError:
        print("Enter a valid amount.")
        return

    accounts[account_no] = {
        "name": name,
        "phone": phone,
        "balance": initial_deposit
    }

    save_accounts(accounts)

    print("\nAccount created successfully!")
    print("Account Number:", account_no)


def check_balance(accounts):
    account_no = input("Enter account number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    print("Account Holder:", accounts[account_no]["name"])
    print("Balance: ₹", accounts[account_no]["balance"])


def deposit(accounts):
    account_no = input("Enter account number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Enter a positive amount.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    accounts[account_no]["balance"] += amount
    save_accounts(accounts)

    print("Amount deposited successfully!")
    print("New Balance: ₹", accounts[account_no]["balance"])


def withdraw(accounts):
    account_no = input("Enter account number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a positive amount.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    balance = accounts[account_no]["balance"]

    if amount > balance:
        print("Insufficient balance!")
        return

    accounts[account_no]["balance"] -= amount
    save_accounts(accounts)

    print("Amount withdrawn successfully!")
    print("Remaining Balance: ₹", accounts[account_no]["balance"])


def transfer_money(accounts):
    sender = input("Enter sender account number: ")
    receiver = input("Enter receiver account number: ")

    if sender not in accounts:
        print("Sender account not found!")
        return

    if receiver not in accounts:
        print("Receiver account not found!")
        return

    if sender == receiver:
        print("Cannot transfer to the same account.")
        return

    try:
        amount = float(input("Enter transfer amount: "))

        if amount <= 0:
            print("Enter a positive amount.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    if amount > accounts[sender]["balance"]:
        print("Insufficient balance!")
        return

    accounts[sender]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    save_accounts(accounts)

    print("Money transferred successfully!")


def account_details(accounts):
    account_no = input("Enter account number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    account = accounts[account_no]

    print("\n========== ACCOUNT DETAILS ==========")
    print("Account Number :", account_no)
    print("Name           :", account["name"])
    print("Phone          :", account["phone"])
    print("Balance        : ₹", account["balance"])


def delete_account(accounts):
    account_no = input("Enter account number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    if accounts[account_no]["balance"] != 0:
        print("Account balance must be zero before deletion.")
        return

    del accounts[account_no]
    save_accounts(accounts)

    print("Account deleted successfully!")


def main():
    accounts = load_accounts()

    while True:

        print("\n========== BANK MANAGEMENT SYSTEM ==========")
        print("1. Create Account")
        print("2. Account Details")
        print("3. Check Balance")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Transfer Money")
        print("7. Delete Account")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            account_details(accounts)

        elif choice == "3":
            check_balance(accounts)

        elif choice == "4":
            deposit(accounts)

        elif choice == "5":
            withdraw(accounts)

        elif choice == "6":
            transfer_money(accounts)

        elif choice == "7":
            delete_account(accounts)

        elif choice == "8":
            print("Thank you for using Bank Management System!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()