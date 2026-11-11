📒 Contact Book Application

A simple and user-friendly Contact Book Application developed using Python. This application helps users manage their personal contacts by adding, viewing, searching, updating, and deleting contact information.

The project uses JSON file handling to store contact details permanently, so the information remains available even after closing the application.

---

🚀 Project Overview

The Contact Book Application is a menu-driven Python program designed to make contact management easy and efficient.

Users can store important contact information such as names, phone numbers, and email addresses. It also includes input validation and duplicate checking to maintain accurate contact records.

✨ Features

- Add Contact: Add new contacts with name, phone number, and email address.
- View Contacts: Display all saved contacts.
- Search Contact: Search for contacts using their name, phone number, or email address.
- Edit Contact: Update existing contact information.
- Delete Contact: Remove unwanted contacts with confirmation.
- Phone Number Validation: Ensures that phone numbers contain exactly 10 digits.
- Email Validation: Checks whether the entered email address follows a valid format.
- Duplicate Prevention: Prevents adding contacts with an existing phone number or email address.
- JSON Data Storage: Saves contact information permanently using a JSON file.

🛠️ Technologies Used

Technology| Purpose
Python| Core programming language
JSON| Data storage
Regular Expressions (re)| Email validation
File Handling| Reading and writing contact data
OOP| Organizing the application using classes and objects

📂 Project Structure

Contact-Book/
│
├── main.py
│
├── contacts.json
│
├── README.md
│
└── .gitignore

File Description:

- "main.py" – Contains the complete Python source code.
- "contacts.json" – Stores contact details in JSON format.
- "README.md" – Provides project documentation.
- ".gitignore" – Specifies files Git should ignore.

⚙️ Installation and Setup

Step 1: Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL

Step 2: Navigate to the Project Folder

cd Contact-Book

Step 3: Run the Application

python main.py

Requirements:

- Python 3.8 or above.
- VS Code or any Python-supported IDE.
- No external libraries are required.

💻 Application Menu

When you run the program, the following menu will appear:

========== CONTACT BOOK ==========

1. Add Contact
2. View Contacts
3. Search Contact
4. Edit Contact
5. Delete Contact
6. Exit

Enter your choice (1-6):

📸 Sample Output

1. Add Contact

--- ADD CONTACT ---

Enter name: Sona
Enter 10-digit phone number: 9876543210
Enter email: sona@gmail.com

Contact added successfully!

2. View Contacts

--- ALL CONTACTS ---

Contact 1
Name : Sona
Phone: 9876543210
Email: sona@gmail.com

3. Search Contact

--- SEARCH CONTACT ---

Enter name, phone or email: Sona

Contact found!
Name : Sona
Phone: 9876543210
Email: sona@gmail.com

4. Edit Contact

--- EDIT CONTACT ---

Contact updated successfully!

5. Delete Contact

--- DELETE CONTACT ---

Contact deleted successfully!

🧠 Python Concepts Implemented

This project demonstrates the practical implementation of the following Python concepts:

1. Object-Oriented Programming (OOP): Classes, objects, constructors, and methods.
2. Functions: Reusable functions for different operations.
3. Lists: Storing multiple contact records.
4. Dictionaries: Representing individual contact details.
5. Conditional Statements: Managing menu options and validation.
6. Loops: Iterating through contact records.
7. File Handling: Reading and writing data into files.
8. JSON Module: Storing and retrieving structured data.
9. Regular Expressions: Validating email addresses.
10. Exception Handling: Handling file-related errors.
11. CRUD Operations: Create, Read, Update, and Delete contact records.

🔄 CRUD Operations

The application implements all four basic CRUD operations:

Operation| Functionality
Create| Add new contacts
Read| View and search contacts
Update| Edit existing contacts
Delete| Remove contacts

🔐 Data Storage

Contact information is stored in "contacts.json" in JSON format.

Example:

[
    {
        "name": "Sona",
        "phone": "9876543210",
        "email": "sona@gmail.com"
    }
]

The application automatically updates the JSON file whenever contacts are added, edited, or deleted.

🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Developing real-world Python applications.
- Understanding Object-Oriented Programming.
- Implementing CRUD operations.
- Working with JSON files.
- Validating user inputs.
- Managing data using Python lists and dictionaries.
- Handling errors and improving application reliability.

🔮 Future Enhancements

Some features that can be added in future versions:

- Graphical User Interface (GUI) using Tkinter.
- Database integration using SQLite or MySQL.
- Contact sorting and filtering.
- Contact profile pictures.
- Import and export contacts.
- Advanced search functionality.

👩‍💻 Developed By

Sona V O

Python Developer Intern

🙏 Acknowledgement

This project was developed as part of my Python Developer Internship at Cognorise Info Tech.

I am grateful for the opportunity to improve my programming knowledge and gain practical experience through project development.

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback!
