import json
import re
import os

# Load contacts from JSON file
def load_contacts():
    if not os.path.exists("contacts.json"):
        return []

    try:
        with open("contacts.json", "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []

# Save contacts into JSON file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

class ContactBook:

    def __init__(self):
        self.contacts = load_contacts()

    # Validate email
    def validate_email(self, email):
        pattern = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    # Validate phone number
    def validate_phone(self, phone):
        return phone.isdigit() and len(phone) == 10

    # Add contact
    def add_contact(self):
        print("\n--- ADD CONTACT ---")

        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()

        if not name:
            print("Name cannot be empty!")
            return

        if not self.validate_phone(phone):
            print("Invalid phone number! Enter 10 digits.")
            return

        if not self.validate_email(email):
            print("Invalid email address!")
            return

        for contact in self.contacts:
            if contact["phone"] == phone or contact["email"].lower() == email.lower():
                print("Duplicate contact found!")
                return

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        self.contacts.append(contact)
        save_contacts(self.contacts)

        print("Contact added successfully!")

    # View all contacts
    def view_contacts(self):
        print("\n--- ALL CONTACTS ---")

        if not self.contacts:
            print("No contacts available!")
            return

        for index, contact in enumerate(self.contacts, start=1):
            print(f"\nContact {index}")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])

    # Search contact
    def search_contact(self):
        print("\n--- SEARCH CONTACT ---")

        keyword = input("Enter name, phone or email: ").strip().lower()

        if not keyword:
            print("Search field cannot be empty!")
            return

        found = False

        for contact in self.contacts:
            if (keyword in contact["name"].lower()
                    or keyword in contact["phone"]
                    or keyword in contact["email"].lower()):

                print("\nContact Found!")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True

        if not found:
            print("Contact not found!")

    # Edit contact
    def edit_contact(self):
        print("\n--- EDIT CONTACT ---")

        phone = input("Enter phone number of contact to edit: ").strip()

        for contact in self.contacts:
            if contact["phone"] == phone:

                print("Current details:")
                print(contact)

                name = input("Enter new name (press Enter to skip): ").strip()
                new_phone = input("Enter new phone (press Enter to skip): ").strip()
                email = input("Enter new email (press Enter to skip): ").strip()

                if name:
                    contact["name"] = name

                if new_phone:
                    if not self.validate_phone(new_phone):
                        print("Invalid phone number!")
                        return

                    if any(c["phone"] == new_phone and c is not contact
                           for c in self.contacts):
                        print("Phone number already exists!")
                        return

                    contact["phone"] = new_phone

                if email:
                    if not self.validate_email(email):
                        print("Invalid email!")
                        return

                    if any(c["email"].lower() == email.lower() and c is not contact
                           for c in self.contacts):
                        print("Email already exists!")
                        return

                    contact["email"] = email

                save_contacts(self.contacts)
                print("Contact updated successfully!")
                return

        print("Contact not found!")

    # Delete contact
    def delete_contact(self):
        print("\n--- DELETE CONTACT ---")

        phone = input("Enter phone number to delete: ").strip()

        for contact in self.contacts:
            if contact["phone"] == phone:

                print("Contact:", contact)

                confirm = input("Are you sure? (yes/no): ").strip().lower()

                if confirm == "yes":
                    self.contacts.remove(contact)
                    save_contacts(self.contacts)
                    print("Contact deleted successfully!")
                else:
                    print("Deletion cancelled!")

                return

        print("Contact not found!")

# Main menu
def main():

    book = ContactBook()

    while True:

        print("\n========== CONTACT BOOK ==========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            book.add_contact()

        elif choice == "2":
            book.view_contacts()

        elif choice == "3":
            book.search_contact()

        elif choice == "4":
            book.edit_contact()

        elif choice == "5":
            book.delete_contact()

        elif choice == "6":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main()