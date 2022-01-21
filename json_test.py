import json
contacts = {"contacts": [{"first_name": "Tim", "last_name" : "Ruscica"}] }

with open("contacts.json", "w") as f:
    json.dump(contacts, f)  # writes a Python dictionary as json file

with open("contacts.json", "r") as f:
    contacts = json.load(f)  # loads the file as a Python dictionary

print(contacts)  