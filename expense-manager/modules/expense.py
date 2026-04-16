# expenses = []

# def add_expense():
#     try:
#         amount = float(input("Enter amount: "))
#     except ValueError:
#         print("Invalid amount! Please enter a number.")
#         return

#     category = input("Enter category: ")
#     date = input("Enter date: ")
#     description = input("Enter description: ")

#     expense = {
#         "amount": amount,
#         "category": category,
#         "date": date,
#         "description": description
#     }

#     expenses.append(expense)

#     print("Expense added successfully!")

# def view_expenses():
#     if not expenses:
#         print("No expenses found")
#     else:
#         for index, expense in enumerate(expenses, start=1):
#             print(f"\nExpense {index}:")
#             print(f"Amount: {expense['amount']}")
#             print(f"Category: {expense['category']}")
#             print(f"Date: {expense['date']}")
#             print(f"Description: {expense['description']}")  


# def update_expense():
#     if not expenses:
#         print("No expense found")
#         return

#     view_expenses()

#     try:
#         user_choice = int(input("Enter expense number to update: "))
#     except ValueError:
#         print("Invalid input! Please enter a number.")
#         return

#     index = user_choice - 1

#     if index < 0 or index >= len(expenses):
#         print("Invalid choice")
#     else:
#         try:
#             new_amount = float(input("Enter new amount: "))
#         except ValueError:
#             print("Invalid amount!")
#             return

#         new_category = input("Enter new category: ")
#         new_date = input("Enter new date: ")
#         new_description = input("Enter new description: ")

#         expenses[index]["amount"] = new_amount
#         expenses[index]["category"] = new_category
#         expenses[index]["date"] = new_date
#         expenses[index]["description"] = new_description

#         print("Expense updated successfully!")
    
    
# def delete_expense():
#     if not expenses:
#         print("No expense found")
#         return

#     view_expenses()

#     try:
#         user_choice = int(input("Enter expense number to delete: "))
#     except ValueError:
#         print("Invalid input! Please enter a number.")
#         return

#     index = user_choice - 1

#     if index < 0 or index >= len(expenses):
#         print("Invalid choice")
#     else:
#         expenses.pop(index)
#         print("Expense deleted successfully")


from db.connection import connect_db, close_db

# ------------------ ADD EXPENSE ------------------
def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    category_name = input("Enter category (e.g., Food, Travel): ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")

    connection = connect_db()
    if not connection:
        return

    cursor = connection.cursor()

    try:
        # Step 1: Check if category exists
        cursor.execute("SELECT id FROM categories WHERE name = %s", (category_name,))
        result = cursor.fetchone()

        if result:
            category_id = result[0]
        else:
            # Step 2: Insert new category
            cursor.execute(
                "INSERT INTO categories (name) VALUES (%s) RETURNING id",
                (category_name,)
            )
            category_id = cursor.fetchone()[0]

        # Step 3: Insert expense
        cursor.execute(
            """
            INSERT INTO expenses (amount, category_id, date, description)
            VALUES (%s, %s, %s, %s)
            """,
            (amount, category_id, date, description)
        )

        connection.commit()
        print("Expense added successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        close_db(connection)


# ------------------ VIEW EXPENSES ------------------
def view_expenses():
    connection = connect_db()
    if not connection:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT e.id, e.amount, c.name, e.date, e.description
            FROM expenses e
            JOIN categories c ON e.category_id = c.id
            ORDER BY e.id
        """)

        rows = cursor.fetchall()

        if not rows:
            print("No expenses found")
            return

        for index, row in enumerate(rows, start=1):
            print(f"\nExpense {index}:")
            print(f"ID: {row[0]}")
            print(f"Amount: {row[1]}")
            print(f"Category: {row[2]}")
            print(f"Date: {row[3]}")
            print(f"Description: {row[4]}")

        return rows  # VERY IMPORTANT for update/delete

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        close_db(connection)


# ------------------ UPDATE EXPENSE ------------------
def update_expense():
    rows = view_expenses()
    if not rows:
        return

    try:
        choice = int(input("Enter expense number to update: "))
    except ValueError:
        print("Invalid input!")
        return

    if choice < 1 or choice > len(rows):
        print("Invalid choice")
        return

    expense_id = rows[choice - 1][0]

    try:
        new_amount = float(input("Enter new amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    new_category = input("Enter new category: ")
    new_date = input("Enter new date: ")
    new_description = input("Enter new description: ")

    connection = connect_db()
    if not connection:
        return

    cursor = connection.cursor()

    try:
        # Handle category
        cursor.execute("SELECT id FROM categories WHERE name = %s", (new_category,))
        result = cursor.fetchone()

        if result:
            category_id = result[0]
        else:
            cursor.execute(
                "INSERT INTO categories (name) VALUES (%s) RETURNING id",
                (new_category,)
            )
            category_id = cursor.fetchone()[0]

        # Update expense
        cursor.execute("""
            UPDATE expenses
            SET amount = %s, category_id = %s, date = %s, description = %s
            WHERE id = %s
        """, (new_amount, category_id, new_date, new_description, expense_id))

        connection.commit()
        print("Expense updated successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        close_db(connection)


# ------------------ DELETE EXPENSE ------------------
def delete_expense():
    rows = view_expenses()
    if not rows:
        return

    try:
        choice = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Invalid input!")
        return

    if choice < 1 or choice > len(rows):
        print("Invalid choice")
        return

    expense_id = rows[choice - 1][0]

    connection = connect_db()
    if not connection:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
        connection.commit()
        print("Expense deleted successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        close_db(connection)