import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from the file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContacts List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")

# Search for a contact by name or phone number
def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").strip()
    found = False
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            found = True
    if not found:
        print("No matching contact found.")

# Update an existing contact
def update_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print(f"Updating contact '{contact['name']}':")
            contact['name'] = input(f"Enter new name ({contact['name']}): ").strip() or contact['name']
            contact['phone'] = input(f"Enter new phone number ({contact['phone']}): ").strip() or contact['phone']
            contact['email'] = input(f"Enter new email address ({contact['email']}): ").strip() or contact['email']
            contact['address'] = input(f"Enter new address ({contact['address']}): ").strip() or contact['address']
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f"Contact '{removed_contact['name']}' deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Book Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()