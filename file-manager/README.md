📁 File Manager - Python CLI Tool
A simple yet powerful command-line file management system built with Python that allows users to perform essential file and folder operations through an interactive menu-driven interface.

🌟 Features
📂 Folder Operations
Create Folders - Create new directories with custom names and nested paths
Rename Folders - Change folder names with validation checks
Delete Folders - Remove folders with safety confirmation for non-empty directories
Recursive Listing - View all folders and subfolders in the directory tree
📄 File Operations
Create Files - Create new files with optional initial content
Read Files - Display complete file contents in the console
Update Files - Three flexible update options:
✏️ Rename files
🔄 Overwrite content completely
➕ Append to existing content
Delete Files - Remove files with confirmation prompts
🛡️ Safety Features
Input Validation - Ensures all user inputs are valid and safe
Confirmation Prompts - Prevents accidental deletions
Existence Checks - Verifies files/folders exist before operations
Error Handling - Graceful handling of common filesystem errors
Empty Name Protection - Prevents creation of files/folders with empty names
🎨 User Experience
Clear Screen - Clean console display for better readability
Colored Indicators - Visual feedback with ✓ symbols for successful operations
Interactive Menu - Easy-to-navigate numbered menu system
Pause After Operations - "Press Enter to continue" for better control
📋 Prerequisites
Before running this file manager, make sure you have:

Python 3.6 or higher
No external dependencies required (uses only Python standard library)
🚀 Installation
Clone the repository
bash
git clone <https://github.com/MeetBataviya13/file-manager.git>
cd file-manager
Run the program
bash
python file_manager.py
That's it! No pip installations needed. 🎉

💻 Usage
When you run the program, you'll see an interactive menu:

==============================
      FILE MANAGER
==============================

1. Create a folder
2. List files and folders
3. Rename a folder
4. Delete a folder
5. Create a file
6. Read a file
7. Update a file
8. Delete a file
9. Clear screen
0. Exit
==============================
Simply enter the number corresponding to the operation you want to perform and follow the prompts!

📖 Example Operations
Creating a Folder
Enter your choice: 1
Enter folder name: projects/python/my_app
✓ Folder 'projects/python/my_app' created successfully!
Creating a File with Content
Enter your choice: 5
Enter file name (with extension): hello.txt
Enter file content (press Enter for empty file): Hello, World! This is my first file.
✓ File 'hello.txt' created successfully!
Reading a File
Enter your choice: 6
Enter file name to read: hello.txt

--- File Content ---
Hello, World! This is my first file.
--- End of File ---
Updating a File
Enter your choice: 7
Enter file name to update: hello.txt

--- Update Options ---

1. Rename file
2. Overwrite file content
3. Append to file content

Enter your choice: 3
Enter content to append: Adding a new line!
✓ Content appended successfully!
Deleting with Safety Confirmation
Enter your choice: 4
Enter folder name to delete: old_project
Warning: Folder 'old_project' is not empty!
This will delete the folder and ALL its contents. Continue? (y/n): y
✓ Folder 'old_project' deleted successfully!
🏗️ Project Structure
file-manager/
├── file_manager.py      # Main application file
├── README.md           # Project documentation

🛠️ Technologies Used
Python - Core programming language
pathlib - Modern filesystem path operations
os - Operating system interface
shutil - High-level file operations
platform - Cross-platform system information
🎓 Educational Purpose
This project is designed for educational purposes to demonstrate:

✅ File I/O operations in Python
✅ User input handling and validation
✅ Exception handling and error management
✅ Command-line interface (CLI) design patterns
✅ Working with Python's pathlib module
✅ Cross-platform compatibility considerations
✅ Safe file system operations
Perfect for beginners learning Python file handling! 🎯

🤝 Contributing
Contributions are welcome! If you'd like to improve this project:

Fork the repository
Create a new branch (git checkout -b feature/improvement)
Make your changes
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/improvement)
Create a Pull Request
💡 Future Enhancements
 Add file search functionality
 Implement file copying and moving operations
 Add file compression/decompression support
 Include file metadata display (size, date modified, permissions)
 Add batch operations (multi-file operations)
 Implement undo/redo functionality
 Add color-coded output for better UX
 Include file content search
 Add support for hidden files toggle
 Implement favorite/bookmark directories
⚠️ Important Notes
This tool operates on the current working directory
Be careful when deleting files and folders
The recursive listing feature shows all nested items
Always read confirmation prompts carefully
Test operations on non-critical files first
📄 License
This project is open source and available for educational purposes only. Feel free to use, modify, and learn from this code for educational projects and personal learning.

Educational Use Only - This project is intended for learning and educational purposes.

👨‍💻 Author
Meet Bataviya

GitHub: @MeetBataviya13
🙏 Acknowledgments
Built as a learning project to understand file system operations and command-line application development in Python. Special thanks to the Python community for excellent documentation!

Enjoy managing your files! 🎉
If you found this project helpful for learning, please consider giving it a ⭐ on GitHub!

Happy Coding! 💻✨
