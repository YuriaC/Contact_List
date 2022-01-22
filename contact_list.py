from distutils.ccompiler import new_compiler
import email
from operator import ne


class Contacts:
    num_existing_contact_lst = 0

    def __init__(self):
        self.contact_list = []
        self.contatc_num = 0

    @staticmethod
    def phone_num_validation(string):
        new_string ="".join(string.split("-"))
        if new_string.isdigit():
            if len(new_string) == 10:  # legitimate US phone number should be 10-digit long 
                new_string = int(new_string)
        
        else:
            print("This is not a valid phone number.")
            return False


    def add_contact(self):
        """method for adding a contact."""
        new_contact = {}
        f_name = input("First Name: ")
        l_name = input("Last Name: ")
        mobile_num = input("Mobile Phone Number (optional): ")
        home_num = input("Home Phone Number(optional): ")
        email_address = input("Email Address (optional): ")
        address = input("Address (optional): ")
        
        new_contact["first name"] = f_name
        new_contact["last name"] = l_name
        new_contact["mobile phone number"] = mobile_num 
        new_contact["home phone number"] = home_num
        new_contact["email address"] = email_address
        new_contact["address"] = address
        self.contatc_num += 1

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
