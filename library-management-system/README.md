# 📚 Library Management System

A modern, user-friendly library management system built with Python and Streamlit. This system provides an intuitive web interface for managing books, members, and borrowing operations.

## ✨ Features

- **📖 Book Management**
  - Add new books with title, author, and quantity
  - View all books with real-time availability status
  - Search books by title or author
  - Automatic unique ID generation for each book

- **👥 Member Management**
  - Register new library members
  - Store member information (name, email)
  - Track borrowed books per member
  - Automatic unique ID generation for each member

- **📤📥 Borrowing System**
  - Borrow books with member selection
  - Track borrowing date and time
  - Return books with easy selection
  - Automatic inventory updates

- **📊 Dashboard**
  - View total books, copies, and members
  - Recent activity tracking
  - Real-time statistics

- **💾 Data Persistence**
  - All data stored in JSON format
  - Automatic save on every operation
  - Data preserved across sessions

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/MeetBataviya13/Python-Projects.git
```

2. Navigate to the project directory:
```bash
cd library-management-system
```

3. Install required dependencies:
```bash
pip install streamlit
```

### Running the Application

Run the Streamlit app:
```bash
streamlit run main_stream.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

## 📖 Usage

### Dashboard (Home)
- View quick statistics about your library
- See recently added books
- Get an overview of total books, copies, and members

### Book Management
- **View Books**: Browse all books, search by title/author
- **Add Book**: Click the "Add Book" tab and fill in the form
  - Enter book title
  - Enter author name
  - Specify number of copies

### Member Management
- **View Members**: See all registered members and their borrowed books
- **Add Member**: Click the "Add Member" tab and fill in the form
  - Enter member name
  - Enter email address

### Borrow a Book
1. Select a member from the dropdown
2. Choose an available book
3. Click "Borrow Book"

### Return a Book
1. Select a member who has borrowed books
2. Choose the book to return from their borrowed list
3. Click "Return Book"

## 📁 Project Structure

```
library-management-system/
│
├── main_stream.py            # Main Streamlit application
├── main_cli.py             #Main Cli version             
├── data.json               # JSON database file
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 💾 Data Storage

The system stores data in `data.json` with the following structure:

```json
{
    "books": [
        {
            "id": "B-XXXXX",
            "title": "Book Title",
            "author": "Author Name",
            "available_copies": 5,
            "total_copies": 5,
            "added_on": "2025-12-03 12:00:00"
        }
    ],
    "members": [
        {
            "id": "M-XXXXX",
            "name": "Member Name",
            "email": "member@email.com",
            "borrowed": []
        }
    ]
}
```

## 🛠️ Technical Details

- **Language**: Python 3.7+
- **Framework**: Streamlit
- **Data Format**: JSON
- **ID Generation**: Random 5-character alphanumeric codes
- **Date Format**: YYYY-MM-DD HH:MM:SS

## 📦 Dependencies

```
streamlit>=1.28.0
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Advanced search and filtering
- [ ] Due date tracking and overdue notifications
- [ ] Fine calculation system
- [ ] Book reservation system
- [ ] Export reports to CSV/PDF
- [ ] User authentication and roles
- [ ] Database integration (SQLite/MySQL/PostgreSQL)
- [ ] Book cover images
- [ ] Email notifications
- [ ] Mobile responsive design improvements

## 📄 License

This project is open source and educational purpose only.

## 👤 Author

**Meet Bataviya**
- GitHub: [@MeetBataviya13](https://github.com/MeetBataviya13)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Thanks to the Python community
- Inspired by real-world library management needs

---

⭐ **Star this repository if you find it helpful!**

## 🐛 Known Issues

If you encounter any issues, please [open an issue](https://github.com/MeetBataviya13/library-management-system/issues) on GitHub.

## 📞 Support

For support and questions, please open an issue in the GitHub repository.
