import json
import re

def is_valid_phone(phone):
    return re.match(r'^\+?[0-9]+$', phone) is not None

def is_valid_email(email):
    return re.match(r'^[^@]+@[^@]+\.[^@]+$', email) is not None

def load_contacts():
    try:
        with open('contacts.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts):
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    if not phone:
        print("Phone number cannot be empty.")
        return
    if not is_valid_phone(phone):
        print("Invalid phone number. Must be digits optionally starting with +.")
        return
    email = input("Enter email: ").strip()
    if not email:
        print("Email cannot be empty.")
        return
    if not is_valid_email(email):
        print("Invalid email address.")
        return
    contacts[name] = {'phone': phone, 'email': email}
    print("Contact added successfully.")

def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    contact = contacts.get(name)
    if contact:
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    contact = contacts[name]
    print("Leave blank to keep current value.")
    phone = input(f"New phone ({contact['phone']}): ").strip()
    if phone:
        if is_valid_phone(phone):
            contact['phone'] = phone
        else:
            print("Invalid phone; keeping old value.")
    email = input(f"New email ({contact['email']}): ").strip()
    if email:
        if is_valid_email(email):
            contact['email'] = email
        else:
            print("Invalid email; keeping old value.")
    print("Contact updated.")

def view_all_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
        return
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")

def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. View All Contacts")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            view_all_contacts(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Exiting. Your contacts have been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()