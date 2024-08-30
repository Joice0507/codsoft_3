contacts = {}
def add_contact():
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")

    if not phone_number.isdigit():
        print("Invalid phone number. Please enter digits only.")
        return

    contacts[name] = phone_number
    print("Contact added successfully!")

def view_contacts():
    if contacts:
        print("\nContact List:")
        print("Name\t\t\tPhone Number")
        for name, phone_number in contacts.items():
            print(f"{name}\t\t\t{phone_number}")
    else:
        print("No contacts available.")

def search_contact():
    search_term = input("\nEnter the name of the contact you want to search for: ")

    if search_term in contacts:
        print(f"Name: {search_term}, Phone Number: {contacts[search_term]}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact you want to update: ")

    if name in contacts:
        new_phone_number = input("Enter the new phone number: ")
        if not new_phone_number.isdigit():
            print("Invalid phone number. Please enter digits only.")
            return
        contacts[name] = new_phone_number
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def contact_log():
    while True:
        print("\n--- Contact Log ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Log.")
            break
        else:
            print("Invalid option. Please choose a valid number.")


contact_log()
