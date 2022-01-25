import json

class Contacts:
    # num_existing_contact_lst = 0  #
    file_path = "contacts.json"
        
    def __init__(self): 
        self.contact_list = self.read_contacts(Contacts.file_path)
       
    def read_contacts(self, file_path):
        """a method serves to load contact data from an existing json file. An empty dict will be created
        upon the case that file not found. Returns a dict obj"""
        try:
            with open(file_path, 'r') as file:  # loads the file as a Python dictionary
                contact_list = json.load(file)
        except FileNotFoundError:  # if file failed to open, then create a new dict obj to store data 
            contact_list = dict()

        return contact_list   

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
        identifier = splitted_email[: -1]
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
    def check_if_user_input_is_empty(prompt):
        """this method helps to get user input and check if the input string is empty, returns either str or Bool type"""
        response = input(prompt)
        new_string = response.strip(" ")
            
        if len(new_string) > 0:
            return new_string

        else:
            return False 

    def ask_for_contact_name(self):
        """a method that constantly ask for contant's name until non-empty values are given by user input. 
        Returns a lst obj"""
        credential = []
        
        while True:  # keep asking for input until an non-empty input is given
            f_name = Contacts.check_if_user_input_is_empty("First Name: ")  # get user input for f_name
            if not f_name:
                print("Input cannot be empty!")
                
            else:
                credential.append(f_name.lower())
                break
        
        while True:  # keep asking for input until an non-empty input is given
            l_name = Contacts.check_if_user_input_is_empty("Last Name: ")  # get user input for l_name
            if not l_name:
                print("Input cannot be empty!")
                
            else:
                credential.append(l_name.lower())
                break
        
        return credential

    def add_contact(self):  # REVISED
        """method for adding a contact."""
        info = []
        
        contact_name = self.ask_for_contact_name()
        key = contact_name[0] + "_" + contact_name[1]  # key = "{f_name}_{l_name}"

        if key in self.contact_list:
            print("Contact already exists in current contacts list!")
        
        else:
            # register mobile phone number
            mobile_num = Contacts.check_if_user_input_is_empty("Mobile Phone Number (optional): ")
            if not mobile_num:  # when entry is  empty
                print("No response is registered. ")
            
            else:
                cell_validity_check = Contacts.phone_num_validation(mobile_num)  # check if the phone_num is legit
                if cell_validity_check:  # if passed data validation
                    info.append({"mobile phone" : mobile_num})
                
                else: 
                    print("Invalid phone number. This info won't be registered.")

            # register home phone number
            home_num = Contacts.check_if_user_input_is_empty("Home Phone Number(optional): ")
            if not home_num:
                print("No response is registered. ")

            else:
                home_num_validity_check = Contacts.phone_num_validation(home_num)
                if home_num_validity_check:
                    info.append({"home phone" : home_num})
                
                else: 
                    print("Invalid phone number. This info won't be registered.")

            # register email address
            email_address = Contacts.check_if_user_input_is_empty("Email Address (optional): ")
            if not email_address:
                print("No response is registered. ")

            else:
                email_address.lower()
                email_validity_check = Contacts.email_verifier(email_address)
                if email_validity_check:
                    info.append({"email address" : email_address})
                
                else:
                    print("Invalid email address. This info won't be registered.")
            
            # register address
            address = Contacts.check_if_user_input_is_empty("Address (optional): ")
            if not address:
                print("No response is registered. ")
            
            else:
                info.append({"address" : address})
            
            self.contact_list[key] = info   # register new contact's info into the contact list
            print("Contact added!")

    def search_contact(self):  # IMPLEMENTED
        """method for searching for a contact. Takes a lst obj, Return a dict obj"""
        credential = self.ask_for_contact_name()
        pre_selection = dict()
        result = dict()

        for key, value in self.contact_list.items():
            contact_name = key.split("_")

            if credential[0] in contact_name[0]:  # if first name search is successful
                pre_selection[key] = value  # add that contact to a new dictionary
                    
                
        for key, value in pre_selection.items():
            contact_name = key.split("_")
                
            if credential[1] in contact_name[1]:
                result[key] = value

        return result

    def search_result_interpretor(self, result):  # IMPLEMENTED
        """a method that helps to show the search contact result"""
        if len(result) == 0:
            print("No contact found")
            return False

        else: 
            self.list_contacts(result)

    def delete_contact(self):  # IMPLEMENTED
        """method for deleting a contact."""
        resulting_contact = self.search_contact()

        if len(resulting_contact) == 0:
            print("No contact found!")
        
        elif len(resulting_contact) == 1:
            key = list(resulting_contact.keys())[0]  
            self.contact_list.pop(key)
            print("Contact deleted.")
        
        else:
            print("More than 1 contact found. Please specified search creteria!")

    def format_name(self, string):  # NEW ADDITION
        """extracting and formating the name of the contact found"""
        name = string.split("_")
        for n in range(len(name)):
            name[n] = name[n].capitalize()

        full_name = " ".join(name)
        
        return full_name

    def list_contacts(self, dict_obj):  # IMPLEMENTED 
        """method for printing contacts in a contact list in alphabetical order."""
        index = 1
        for key, value in dict_obj.items():
            contact_name = self.format_name(key)  # formatting contact name
            print(f"{index}. {' '.join(contact_name)}")  # print contact name
            for sub_dict_obj in value:
                for k, v in sub_dict_obj.items():
                    print(f"\t{k.capitalize()}: {v}")

            print("")
            index += 1
        
    def save_contacts(self):  # NEW_ADDITION
        """method for saving a contact list."""
        contacts = self.contact_list
        with open("contacts.json", "w") as file:
            json.dump(contacts, file)  # writes a Python dictionary as json file
        
        file.close()

    def edit_contact(self):  # NEW_ADDITION
        """method for editing the info of an existing contact"""
        result = self.search_contact()
        
        if len(result) == 1:  # if exact mathing is found
            key = list(result.keys())[0]  # retrive key for the contact info
            
            contact_name = self.format_name(key)
            print(f"Editing info for contact: {contact_name}")
            
            # getting new info
            new_info = []

            # register mobile phone number
            mobile_num = Contacts.check_if_user_input_is_empty("Mobile Phone Number (optional): ")
            if not mobile_num:  # when entry is  empty
                print("No response is registered. ")
            
            else:
                cell_validity_check = Contacts.phone_num_validation(mobile_num)  # check if the phone_num is legit
                if cell_validity_check:  # if passed data validation
                    new_info.append({"mobile phone" : mobile_num})
                
                else: 
                    print("Invalid phone number. This info won't be registered.")

            # register home phone number
            home_num = Contacts.check_if_user_input_is_empty("Home Phone Number(optional): ")
            if not home_num:
                print("No response is registered. ")

            else:
                home_num_validity_check = Contacts.phone_num_validation(home_num)
                if home_num_validity_check:
                    new_info.append({"home phone" : home_num})
                
                else: 
                    print("Invalid phone number. This info won't be registered.")

            # register email address
            email_address = Contacts.check_if_user_input_is_empty("Email Address (optional): ")
            if not email_address:
                print("No response is registered. ")

            else:
                email_address.lower()
                email_validity_check = Contacts.email_verifier(email_address)
                if email_validity_check:
                    new_info.append({"email address" : email_address})
                
                else:
                    print("Invalid email address. This info won't be registered.")
            
            # register address
            address = Contacts.check_if_user_input_is_empty("Address (optional): ")
            if not address:
                print("No response is registered. ")
            
            else:
                new_info.append({"address" : address})

            # if new info is empty, then don't over write the old info. if new info is not empty, then over write the old info
            
            old_info = self.contact_list[key]  # returns a list obj
            for entry in new_info:
                new_keys = entry.keys()



            for obj in old_info:
                for detail in obj.keys():
                    new_info = self.check_if_user_input_is_empty(detail)
                    if not new_info:
                        print("No response is registered. ")
                    
                    else:
                        obj[detail] = new_info

            print("Contact info updated.")

        elif len(result) == 0:
            print("No contact found.")

        else:
            print("More than 1 contact found. Please specified search creteria!")