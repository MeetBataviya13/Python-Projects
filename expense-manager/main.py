from modules.expense import add_expense, view_expenses, update_expense, delete_expense
from utils.menu import show_menu


def main():
    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            update_expense()
        elif choice == 4:
            delete_expense()
        elif choice == 5:
            print("Thank you !!!")
            break
        else:
            print("Wrong input! Please choose between 1-5.")


if __name__ == "__main__":
    main()