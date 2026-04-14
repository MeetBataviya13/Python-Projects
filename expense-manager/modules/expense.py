expenses = []

def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    category = input("Enter category: ")
    date = input("Enter date: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses found")
    else:
        for index, expense in enumerate(expenses, start=1):
            print(f"\nExpense {index}:")
            print(f"Amount: {expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"Date: {expense['date']}")
            print(f"Description: {expense['description']}")  


def update_expense():
    if not expenses:
        print("No expense found")
        return

    view_expenses()

    try:
        user_choice = int(input("Enter expense number to update: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    index = user_choice - 1

    if index < 0 or index >= len(expenses):
        print("Invalid choice")
    else:
        try:
            new_amount = float(input("Enter new amount: "))
        except ValueError:
            print("Invalid amount!")
            return

        new_category = input("Enter new category: ")
        new_date = input("Enter new date: ")
        new_description = input("Enter new description: ")

        expenses[index]["amount"] = new_amount
        expenses[index]["category"] = new_category
        expenses[index]["date"] = new_date
        expenses[index]["description"] = new_description

        print("Expense updated successfully!")
    
    
def delete_expense():
    if not expenses:
        print("No expense found")
        return

    view_expenses()

    try:
        user_choice = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    index = user_choice - 1

    if index < 0 or index >= len(expenses):
        print("Invalid choice")
    else:
        expenses.pop(index)
        print("Expense deleted successfully")