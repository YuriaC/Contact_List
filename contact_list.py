import email


class Contacts:
    num_existing_contact_lst = 0

    def __init__(self):
        self.contact_list = []
        self.contatc_num = 0

    @staticmethod
    def phone_num_validation(string):
        new_string ="".join(string.split("-"))
        if new_string.isdigit():
            new_string = int(new_string)
        
        else:
            print("This is not a valid phone number.")
            return False


    def add_contact(self):
        """method for adding a contact."""
        f_name = input("First Name: ")
        l_name = input("Last Name: ")
        mobile_num = input("Mobile Phone Number (optional): ")
        home_num = input("Home Phone Number(optional): ")
        email_address = input("Email Address (optional): ")
        address = input("Address (optional): ")

        pass
    
    def delete_contact(self):
        """method for deleting a contact."""
        pass

    def list_contacts(self):
        """method for printing all contacts in a contact list in alphabetical order."""
        pass

    def search_contact(self):
        """method for searching for a contact."""
        pass
    
    def save_contacts(self):
        """method for saving a contact list."""
        pass

    def __repr__(self):
        """method for presenting a Contacts class obj"""
        pass 
