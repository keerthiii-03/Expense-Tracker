import csv
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
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[1].strip().lower() == cat:
                print(" | ".join(row))
                found = True

    if not found:
        print("No expenses found for this category.\n")
    print()


def main():
    while True:
        print("===== Expense Tracker =====")
        print("1 → Add Expense")
        print("2 → View All Expenses")
        print("3 → View by Category")
        print("4 → Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
