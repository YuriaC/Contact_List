# Project Requirement:
[Full Project requirement](https://www.programmingexpert.io/projects/contact-list)  
## Goal: Create a contact list program that can persistently store a list of a user's contacts  

1. Features: your program needs to:  
    1. Create contact  
    1. delete contact  
    1. list contacts  
    1. search contacts  

1. Contact should be stored **persistently**, this means:   
    1. each time the program is executed the contacts added or deleted in previous executions are still accessible  
    1. Created contacts should be stored in a **.json file**.  

1. Each contact in the contact list requires a first name and last name but all other fields are optional:  
    1. The optional fields are:  
        1. Mobile Phone Number: needs to be validated to have 10 digits of number  
        1. Home Phone Number: needs to be validated to have 10 digits of number  
        1. Email Address: also needs to be validated  
        1. Address  

1. Each contact in the list must be unique: meaning no repeating First_Last combination  

1. Your program should **constantly** ask the user to enter one of the following commands:  
    1. add: adds a contact to the contact list  
    1. delete: deletes a contact from the contact list using it's first and last name    
    1. list: list all the contacts in alphabetical order by first name    
    1. search: searches for contacts by their first and last name  
        - search should return all results that contains the searching criteria and display the results in alphabetical order  
    1. q: quits the program and saves all of the current contacts  