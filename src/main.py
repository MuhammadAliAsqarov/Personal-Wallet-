from datetime import datetime
from src.wallet import Wallet
from src.record import Record


def display_menu():
    print("1. Show balance")
    print("2. Add a record")
    print("3. Edit a record")
    print("4. Search records")
    print("5. Exit")


def main():
    wallet = Wallet('../data/records.txt')

    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            income, expenses, balance = wallet.get_balance()
            print(f"Income: {income}\nExpenses: {expenses}\nBalance: {balance}")

        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (Income/Expense): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            wallet.add_record(Record(date, category, amount, description))
            print("Record added successfully.")

        elif choice == '3':
            index = int(input("Enter the index of the record to edit: "))
            date = input("Enter new date (YYYY-MM-DD): ")
            category = input("Enter new category (Income/Expense): ")
            amount = float(input("Enter new amount: "))
            description = input("Enter new description: ")
            wallet.edit_record(index, Record(date, category, amount, description))
            print("Record edited successfully.")

        elif choice == '4':
            search_type = input("Search by category/date/amount: ").lower()
            if search_type == 'category':
                category = input("Enter category: ")
                results = wallet.search_records(category=category)
            elif search_type == 'date':
                date = input("Enter date (YYYY-MM-DD): ")
                results = wallet.search_records(date=date)
            elif search_type == 'amount':
                amount = float(input("Enter amount: "))
                results = wallet.search_records(amount=amount)
            else:
                print("Invalid search type.")
                continue
            for record in results:
                print(record)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
