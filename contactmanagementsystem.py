class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, index, updated_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = updated_contact
            print("Contact updated successfully!")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted successfully!")
        else:
            print("Invalid contact index.")

def get_contact_details():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return Contact(name, phone, email, address)

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            contact = get_contact_details()
            contact_manager.add_contact(contact)

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = contact_manager.search_contact(query)
            if results:
                print("\nSearch Results:")
                for i, contact in enumerate(results, 1):
                    print(f"{i}. {contact.name} - {contact.phone}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            contact_manager.view_contacts()
            index = int(input("Enter the index of the contact to update: ")) - 1
            updated_contact = get_contact_details()
            contact_manager.update_contact(index, updated_contact)

        elif choice == '5':
            contact_manager.view_contacts()
            index = int(input("Enter the index of the contact to delete: ")) - 1
            contact_manager.delete_contact(index)

        elif choice == '6':
            print("Thank you for using the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()