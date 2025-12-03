import random
import string
import json
from pathlib import Path
from datetime import datetime
import streamlit as st

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
    
    @staticmethod
    def add_book(title, author, copies):
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
        return book["id"]
    
    @staticmethod
    def get_all_books():
        return Library.data["books"]

    @staticmethod
    def add_member(name, email):
        member = {
            "id": Library.generate_id("M"),
            "name": name,
            "email": email,
            "borrowed": []
        }
        Library.data["members"].append(member)
        Library.save_data()
        return member["id"]

    @staticmethod
    def get_all_members():
        return Library.data["members"]

    @staticmethod
    def borrow_book(member_id, book_id):
        members = [m for m in Library.data["members"] if m["id"] == member_id]
        if not members:
            return False, "Member not found"
        member = members[0]
        
        books = [b for b in Library.data["books"] if b["id"] == book_id]
        if not books:
            return False, "Book not found"
        book = books[0]
        
        if book["available_copies"] <= 0:
            return False, "No copies available"
        
        borrow_entry = {
            "book_id": book["id"],
            "title": book["title"],
            "borrowed_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        member["borrowed"].append(borrow_entry)
        book['available_copies'] -= 1 
        Library.save_data()
        return True, f"Book '{book['title']}' borrowed successfully!"

    @staticmethod
    def return_book(member_id, book_index):
        members = [m for m in Library.data['members'] if m['id'] == member_id]
        if not members:
            return False, "Member not found"
        
        member = members[0]
        
        if not member['borrowed'] or book_index >= len(member['borrowed']):
            return False, "Invalid selection"
        
        selected = member['borrowed'].pop(book_index)
        
        books = [bk for bk in Library.data['books'] if bk['id'] == selected['book_id']]
        if books:
            books[0]['available_copies'] += 1
        
        Library.save_data()
        return True, f"Book '{selected['title']}' returned successfully!"


def main():
    st.set_page_config(
        page_title="Library Management System",
        page_icon="📚",
        layout="wide"
    )
    
    st.title("📚 Library Management System")
    st.markdown("---")
    
    # Sidebar navigation
    menu = st.sidebar.selectbox(
        "Navigation",
        ["🏠 Home", "📖 Books", "👥 Members", "📤 Borrow Book", "📥 Return Book"]
    )
    
    if menu == "🏠 Home":
        st.header("Welcome to Library Management System")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Books", len(Library.data["books"]))
        
        with col2:
            total_copies = sum(b["total_copies"] for b in Library.data["books"])
            st.metric("Total Copies", total_copies)
        
        with col3:
            st.metric("Total Members", len(Library.data["members"]))
        
        st.markdown("---")
        st.subheader("📊 Recent Activity")
        
        # Show recent books
        if Library.data["books"]:
            st.write("**Recently Added Books:**")
            recent_books = sorted(Library.data["books"], key=lambda x: x["added_on"], reverse=True)[:5]
            for book in recent_books:
                st.write(f"- {book['title']} by {book['author']} (Added: {book['added_on']})")
    
    elif menu == "📖 Books":
        st.header("Book Management")
        
        tab1, tab2 = st.tabs(["📋 View Books", "➕ Add Book"])
        
        with tab1:
            books = Library.get_all_books()
            if not books:
                st.info("No books in the library yet.")
            else:
                st.subheader(f"Total Books: {len(books)}")
                
                # Search functionality
                search = st.text_input("🔍 Search books by title or author", "")
                
                if search:
                    books = [b for b in books if search.lower() in b["title"].lower() or search.lower() in b["author"].lower()]
                
                for book in books:
                    with st.expander(f"📕 {book['title']} - {book['author']}"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**ID:** {book['id']}")
                            st.write(f"**Title:** {book['title']}")
                            st.write(f"**Author:** {book['author']}")
                        with col2:
                            st.write(f"**Total Copies:** {book['total_copies']}")
                            st.write(f"**Available:** {book['available_copies']}")
                            st.write(f"**Added On:** {book['added_on']}")
        
        with tab2:
            st.subheader("Add New Book")
            with st.form("add_book_form"):
                title = st.text_input("Book Title*")
                author = st.text_input("Author*")
                copies = st.number_input("Number of Copies*", min_value=1, value=1)
                
                submitted = st.form_submit_button("Add Book")
                if submitted:
                    if title and author:
                        book_id = Library.add_book(title, author, copies)
                        st.success(f"✓ Book added successfully! ID: {book_id}")
                        st.rerun()
                    else:
                        st.error("Please fill in all required fields.")
    
    elif menu == "👥 Members":
        st.header("Member Management")
        
        tab1, tab2 = st.tabs(["📋 View Members", "➕ Add Member"])
        
        with tab1:
            members = Library.get_all_members()
            if not members:
                st.info("No members registered yet.")
            else:
                st.subheader(f"Total Members: {len(members)}")
                
                for member in members:
                    with st.expander(f"👤 {member['name']} ({member['id']})"):
                        st.write(f"**Email:** {member['email']}")
                        st.write(f"**Borrowed Books:** {len(member['borrowed'])}")
                        
                        if member['borrowed']:
                            st.write("**Currently Borrowed:**")
                            for item in member['borrowed']:
                                st.write(f"- {item['title']} (Borrowed on: {item['borrowed_on']})")
        
        with tab2:
            st.subheader("Register New Member")
            with st.form("add_member_form"):
                name = st.text_input("Name*")
                email = st.text_input("Email*")
                
                submitted = st.form_submit_button("Add Member")
                if submitted:
                    if name and email:
                        member_id = Library.add_member(name, email)
                        st.success(f"✓ Member added successfully! ID: {member_id}")
                        st.rerun()
                    else:
                        st.error("Please fill in all required fields.")
    
    elif menu == "📤 Borrow Book":
        st.header("Borrow Book")
        
        members = Library.get_all_members()
        books = Library.get_all_books()
        
        if not members:
            st.warning("No members registered. Please add members first.")
        elif not books:
            st.warning("No books available. Please add books first.")
        else:
            with st.form("borrow_form"):
                member_options = {f"{m['name']} ({m['id']})": m['id'] for m in members}
                selected_member = st.selectbox("Select Member*", list(member_options.keys()))
                
                available_books = [b for b in books if b['available_copies'] > 0]
                if not available_books:
                    st.error("No books available for borrowing.")
                else:
                    book_options = {f"{b['title']} by {b['author']} ({b['id']}) - Available: {b['available_copies']}": b['id'] for b in available_books}
                    selected_book = st.selectbox("Select Book*", list(book_options.keys()))
                    
                    submitted = st.form_submit_button("Borrow Book")
                    if submitted:
                        member_id = member_options[selected_member]
                        book_id = book_options[selected_book]
                        success, message = Library.borrow_book(member_id, book_id)
                        
                        if success:
                            st.success(message)
                            st.rerun()
                        else:
                            st.error(message)
    
    elif menu == "📥 Return Book":
        st.header("Return Book")
        
        members = Library.get_all_members()
        members_with_books = [m for m in members if m['borrowed']]
        
        if not members_with_books:
            st.info("No borrowed books to return.")
        else:
            with st.form("return_form"):
                member_options = {f"{m['name']} ({m['id']}) - {len(m['borrowed'])} book(s)": m['id'] for m in members_with_books}
                selected_member = st.selectbox("Select Member*", list(member_options.keys()))
                
                member_id = member_options[selected_member]
                member = [m for m in members if m['id'] == member_id][0]
                
                book_options = {f"{i+1}. {b['title']} (Borrowed: {b['borrowed_on']})": i for i, b in enumerate(member['borrowed'])}
                selected_book = st.selectbox("Select Book to Return*", list(book_options.keys()))
                
                submitted = st.form_submit_button("Return Book")
                if submitted:
                    book_index = book_options[selected_book]
                    success, message = Library.return_book(member_id, book_index)
                    
                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
    
    # Footer
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit")


if __name__ == "__main__":
    main()