from contact_list import Contacts

def show_direction_prompt():
    print("\nWelcome to your contact list!\n")
    print("The following is a list of useable commands: ")     
    print("\t\"add\": Adds a contact.\n\t\"delete\": Deletes a contact.\n\t\"list\": Lists all contacts.\n\t\"search\": Searches for a contact by name.\n\t\"q\": Quits the program and saves the contact list.\n")

my_contact = Contacts()

show_direction_prompt()
while True:
    choice = input("Type a command: ")

    if choice.lower() == "add":
        #my_contact.add_contact()  #
        print("Contact added!") #
        pass

    elif choice.lower() == "delete":
        #my_contact.delete_contact()  #
        print("Contact deleted!") #
        pass

    elif choice.lower() == "list":
        #my_contact.list_contacts()  #
        print("contact printed") #
        pass

    elif choice.lower() == "search":
        #my_contact.search_contact()  #
        print("result fetched.") #
        pass

    elif choice.lower() == "q":
        #my_contact.save_contacts()  #
        print("Your contacts were saved successfully. Exiting program...")
        break

    else: 
        print("Invalid command. Please try again.")
    
    print("-----------------------------")