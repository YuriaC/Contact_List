import email


class Contacts:
    num_existing_contact_lst = 0

    def __init__(self):
        self.contact_list =dict()
        self.contatc_num = 0

    @staticmethod
    def phone_num_validation(string):
        """a method for verifying the validity of a phone number. Returns Bool"""
        new_string ="".join(string.split("-"))
        if new_string.isdigit():   
            if len(new_string) == 10:
                return True
            
            else:
                print("This is not a valid phone number.")
                return False
 
        else:
            print("This is not a valid phone number.")
            return False

    @staticmethod
    def email_verifier(email_address):
        """a method for verifying the validity of an email address. Returns Bool"""
        
        if "@" not in email_address: 
            return False
        
        splitted_email = email_address.split("@")
        identifier = splitted_email[":-1"]
        domain = splitted_email[-1]
            
        if "." not in domain: 
            return False
            
        elif len(identifier) < 1:
            return False

        splitted_domain = domain.split(".")

        for section in splitted_domain:
            if len(section) == 0:
                return False
            
        else: 
            return True

    @staticmethod
    def check_if_user_input_is_empty(string):
        """this method helps to check if a user input string is empty, returns Bool type"""
        new_string = string.strip(" ")
        
        if len(new_string) > 0:
            return True

        else:
            return False 

    def add_contact(self):
        """method for adding a contact."""
        info = []
        
        # register first name
        while True:  # keep asking for user input until an non-empty string is given 
            f_name = input("First Name: ")
            not_empty_check = Contacts.check_if_user_input_is_empty(f_name)
            if not not_empty_check:
                print("Must provide contact's first name!")
            
            else: 
                f_name = f_name.capitalize()
                info.append({"first name" : f_name})
                break
        
        # register last name
        while True:  # keep asking for user input until an non-empty string is given 
            l_name = input("Last Name: ")
            not_empty_check = Contacts.check_if_user_input_is_empty(l_name)
            if not not_empty_check:
                print("Must provide contact's last name!")
            
            else:
                l_name = l_name.capitalize()
                info.append({"last name" : l_name})
                break

        # register mobile phone number
        mobile_num = input("Mobile Phone Number (optional): ")
        not_empty_check = Contacts.check_if_user_input_is_empty(mobile_num)
        if not_empty_check:  # when entry is not empty
            cell_validity_check = Contacts.phone_num_validation(mobile_num)  # check if the phone_num is legit
            if cell_validity_check:  # if passed data validation
                info.append({"mobile phone" : mobile_num})

        # register home phone number
        home_num = input("Home Phone Number(optional): ")
        not_empty_check = Contacts.check_if_user_input_is_empty(home_num)
        if not_empty_check:
            home_num_validity_check = Contacts.phone_num_validation(mobile_num)
            if home_num_validity_check:
                info.append({"home phone" : home_num})

        # register email address
        email_address = input("Email Address (optional): ")
        not_empty_check = Contacts.check_if_user_input_is_empty(email_address)
        if not_empty_check:
            email_address.lower()
            email_validity_check = Contacts.email_verifier(email_address)
            if email_validity_check:
                info.append({"email address" : email_address})
        
        # register address
        address = input("Address (optional): ")
        not_empty_check = Contacts.check_if_user_input_is_empty(address)
        if not_empty_check:
            email_address.lower()
            info.append({"address" : address})
        
        key = f_name + "_" + l_name  # key = "{f_name}_{l_name}"
        self.contact_list[key] = info   # register new contact's info into the contact list


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

    def edit_contact(self):
        """method for editing the info of an existing contact"""
        pass

    def __repr__(self):
        """method for presenting a Contacts class obj"""
        pass 
