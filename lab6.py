from typing import Dict, Any


phonebook: Dict[str, Dict[str, str]] = {}


def add_contact() -> None:
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    phonebook[name] = {"phone": phone, "email": email}
    print("Contact added successfully.")


def view_contacts() -> None:
    if not phonebook:
        print("Phonebook is empty.")
        return
    print("\n--- Contacts ---")
    for name, details in phonebook.items():
        print(f"Name : {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}\n")


def search_contact() -> None:
    keyword = input("Enter name to search: ").strip().lower()
    matches = [name for name in phonebook if keyword in name.lower()]
    if matches:
        print("\nMatching contacts:")
        for name in matches:
            print(f"{name} -> Phone: {phonebook[name]['phone']}, Email: {phonebook[name]['email']}")
    else:
        print("No contacts found.")


def update_contact() -> None:
    name = input("Enter name to update: ").strip()
    if name not in phonebook:
        print("Contact not found.")
        return
    phone = input("Enter new phone number: ").strip()
    email = input("Enter new email: ").strip()
    phonebook[name] = {"phone": phone, "email": email}
    print("Contact updated successfully.")


def delete_contact() -> None:
    name = input("Enter name to delete: ").strip()
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


def show_phone_numbers() -> None:
    print("\n--- Phone Numbers ---")
    for name, details in phonebook.items():
        print(f"{name}: {details['phone']}")


def main():
    while True:
        print("\n===== Phonebook =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Show Phone Numbers")
        print("7. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            show_phone_numbers()
        elif choice == "7":
            print("Exiting phonebook...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
