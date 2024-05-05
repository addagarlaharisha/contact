class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                results.append(contact)
        return results

    def update_contact(self, index, new_contact):
        if 0 < index <= len(self.contacts):
            self.contacts[index - 1] = new_contact
        else:
            print("Invalid contact index")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index - 1]
        else:
            print("Invalid contact index")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")
        
        elif choice == '2':
            contact_book.view_contacts()
        
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(query)
            if results:
                print("Search Results:")
                for contact in results:
                    print(f"{contact.name} - {contact.phone_number}, {contact.email}, {contact.address}")
            else:
                print("No matching contacts found.")
        
        elif choice == '4':
            index = int(input("Enter the index of contact to update: "))
            new_name = input("Enter new name: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            new_contact = Contact(new_name, new_phone_number, new_email, new_address)
            contact_book.update_contact(index, new_contact)
            print("Contact updated successfully.")
        
        elif choice == '5':
            index = int(input("Enter the index of contact to delete: "))
            contact_book.delete_contact(index)
            print("Contact deleted successfully.")
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
