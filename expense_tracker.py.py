Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
... import csv
import os

FILE_NAME = "expenses.csv"

def add_expense():
    print("\n=== Add New Expense ===")
    # Take all inputs as strings to avoid syntax errors
    date = input("Enter date (DD-MM-YYYY): ").strip()
    category = input("Enter category: ").strip()
    amount = input("Enter amount: ").strip()
    description = input("Enter description: ").strip()

    # Save to CSV file
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("✅ Expense added successfully!\n")


def view_expenses():
    print("\n=== All Expenses ===")
    if not os.path.exists(FILE_NAME):
        print("No expenses found yet.\n")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))
    print()


def view_by_category():
    print("\n=== View by Category ===")
    if not os.path.exists(FILE_NAME):
        print("No expenses found yet.\n")
        return

    cat = input("Enter category to search: ").strip().lower()
    found = False
    with open(FILE_NAME, "r
