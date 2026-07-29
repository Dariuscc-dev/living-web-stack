from models import Contact
import database

def display_menu():
    print("\n--- 📊 MICRO-CRM CLI ---")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Update Contact Status")
    print("4. Delete Contact")
    print("0. Save & Exit")
    print("------------------------")

def main():
    # 1. Load data from disk to memory (RAM)
    raw_data = database.load_data()
    
    # 2. Convert raw dictionaries into Contact objects (List Comprehension)
    contacts = [Contact.from_dict(item) for item in raw_data]

    # 3. Main Loop
    while True:
        display_menu()
        
        try:
            choice = int(input("Select an option (0-4): "))
        except ValueError:
            print("❌ Error: Please enter a valid number.")
            continue

        if choice == 1:
            print("\n[ ADD CONTACT ]")
            name = input("Name: ")
            role = input("Role/Job Title: ")
            company = input("Company: ")
            linkedin = input("LinkedIn URL: ")
            
            new_contact = Contact(name, role, company, linkedin)
            contacts.append(new_contact)
            print(f"✅ Contact '{name}' added successfully!")

        elif choice == 2:
            print("\n[ CONTACT LIST ]")
            if not contacts:
                print("No contacts found. Add one first!")
            else:
                for c in contacts:
                    print(f"[{c.id}] {c.name} - {c.role} @ {c.company} | Status: {c.status}")

        elif choice == 3:
            print("\n[ UPDATE STATUS ]")
            contact_id = input("Enter the ID of the contact to update: ")
            
            # Find the contact
            found = False
            for c in contacts:
                if c.id == contact_id:
                    new_status = input("Enter new status (e.g., Message Sent, Interview, Hired): ")
                    c.status = new_status
                    print(f"✅ Status updated for '{c.name}'.")
                    found = True
                    break
            
            if not found:
                print("❌ Contact ID not found.")

        elif choice == 4:
            print("\n[ DELETE CONTACT ]")
            contact_id = input("Enter the ID of the contact to delete: ")
            
            # Filter out the deleted contact
            initial_count = len(contacts)
            contacts = [c for c in contacts if c.id != contact_id]
            
            if len(contacts) < initial_count:
                print("✅ Contact deleted successfully.")
            else:
                print("❌ Contact ID not found.")

        elif choice == 0:
            print("\n💾 Saving data to disk...")
            # Convert objects back to dictionaries
            dicts_to_save = [c.to_dict() for c in contacts]
            database.save_data(dicts_to_save)
            print("👋 Data saved. Exiting CRM. Have a great day!")
            break

        else:
            print("❌ Invalid option. Please select a number between 0 and 4.")

if __name__ == "__main__":
    main()
