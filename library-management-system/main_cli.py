import random
import string
import json
from pathlib import Path
from datetime import datetime

class Library:
    database = "library-management/data.json"
    data = {"books": [], "members": []}

    # Ensure directory exists
    Path(database).parent.mkdir(parents=True, exist_ok=True)

    # Load existing data from json or create json
    if Path(database).exists():
        with open(database, "r") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)
    else:
        with open(database, "w") as f:
            json.dump(data, f, indent=4, default=str)
    
    @staticmethod
    def generate_id(prefix="B"):
        random_id = ""
        for i in range(5):
            random_id += random.choice(string.ascii_uppercase + string.digits)
        return prefix + "-" + random_id

    @classmethod
    def save_data(cls):
        with open(cls.database, "w") as f:
            json.dump(cls.data, f, indent=4, default=str)
    
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter the book author: ")
        try:
            copies = int(input("How many copies: "))
        except ValueError:
            print("Invalid number of copies. Book not added.")
            return
        
        book = {
            "id": Library.generate_id(),
            "title": title,
            "author": author,
            "available_copies": copies,
            "total_copies": copies,
            "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        Library.data["books"].append(book)
        Library.save_data()
        print("✓ Book added successfully!")
    
    def list_books(self):
        if not Library.data["books"]:
            print("No books found in the library.")
            return
        
        print("\n" + "="*70)
        print(f"{'ID':<12} {'Title':<25} {'Author':<20} {'Copies'}")
        print("="*70)
        for b in Library.data["books"]:
            print(f"{b['id']:<12} {b['title'][:24]:<25} {b['author'][:19]:<20} {b['available_copies']}/{b['total_copies']}")
        print()

    @staticmethod
    def add_member():
        name = input("Enter the name: ")
        email = input("Please enter the email: ")
        member = {
            "id": Library.generate_id("M"),
            "name": name,
            "email": email,
            "borrowed": []
        }
        Library.data["members"].append(member)
        Library.save_data()
        print("✓ Member added successfully!")

    def list_members(self):
        if not Library.data["members"]:
            print("No members found.")
            return
        
        print("\n" + "="*70)
        print(f"{'ID':<12} {'Name':<25} {'Email':<30}")
        print("="*70)
        for b in Library.data["members"]:
            print(f"{b['id']:<12} {b['name'][:24]:<25} {b['email'][:29]:<30}")
            if b['borrowed']:
                print(f"  Currently borrowed: {len(b['borrowed'])} book(s)")
                for item in b['borrowed']:
                    print(f"    - {item['title']} (borrowed on {item['borrowed_on']})")
        print()

    def borrow_book(self):
        member_id = input("Enter your membership ID: ").strip()
        members = [m for m in Library.data["members"] if m["id"] == member_id]
        if not members:
            print("No such member exists.")
            return
        member = members[0]
        
        book_id = input("Enter book ID: ").strip()
        books = [b for b in Library.data["books"] if b["id"] == book_id]
        if not books:
            print("No such book exists.")
            return
        book = books[0]
        
        if book["available_copies"] <= 0:
            print("Sorry, no copies available.")
            return
        
        borrow_entry = {
            "book_id": book["id"],
            "title": book["title"],
            "borrowed_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        member["borrowed"].append(borrow_entry)
        book['available_copies'] -= 1 
        Library.save_data()
        print(f"✓ Book '{book['title']}' borrowed successfully!")

    def return_book(self):
        member_id = input("Enter the member ID: ").strip()
        members = [m for m in Library.data['members'] if m['id'] == member_id]
        if not members:
            print("No such member ID exists.")
            return 
        
        member = members[0]

        if not member['borrowed']:
            print("No borrowed books to return.")
            return 
        
        print("\nBorrowed books:")
        for i, b in enumerate(member['borrowed'], start=1):
            print(f"{i}. {b['title']} ({b['book_id']}) - Borrowed on {b['borrowed_on']}")
        
        try:
            choice = int(input("Enter number to return: "))
            if choice < 1 or choice > len(member['borrowed']):
                print("Invalid choice.")
                return
            selected = member['borrowed'].pop(choice - 1)
        except (ValueError, IndexError):
            print("Invalid input.")
            return
        
        books = [bk for bk in Library.data['books'] if bk['id'] == selected['book_id']]
        if books:
            books[0]['available_copies'] += 1
        
        Library.save_data()
        print(f"✓ Book '{selected['title']}' returned successfully!")


def main():
    lib = Library()
    
    while True:
        print("\n" + "="*30)
        print("      LIBRARY MANAGEMENT")
        print("="*30)
        print("1. Add book")
        print("2. List books")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Add member")
        print("6. List members")
        print("0. Exit")
        print("="*30)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            lib.add_book()
        elif choice == 2:
            lib.list_books()
        elif choice == 3:
            lib.borrow_book()
        elif choice == 4:
            lib.return_book()
        elif choice == 5:
            lib.add_member()
        elif choice == 6:
            lib.list_members()    
        elif choice == 0:
            print("Thank you for using Library Management System!")
            break
        else:
            print("Invalid choice. Please select 0-6.")


if __name__ == "__main__":
    main()