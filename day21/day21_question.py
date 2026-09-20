Day 21: Simple Contact Book Using a Dictionary

Concepts used:
 Python dict — creating,
 adding keys, updating,
 deleting,
 checking membership

Problem Statement
Write a Python program that manages a contact book using a dictionary, where the name is the key and the phone number is the value. Menu:
1. Add Contact
2. View Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Exit

New concept: Dictionary basics (you already used one on Day 18, this goes deeper)
contacts = {}                          # empty dictionary
contacts["Arun"] = "9876543210"        # add a new key-value pair
contacts["Arun"] = "9999999999"        # updating works the SAME way — just overwrite
print(contacts["Arun"])                # → "9999999999"  (access by key)

if "Arun" in contacts:                 # check if a key exists
    print("Found!")

del contacts["Arun"]                   # delete a key-value pair

for name in contacts:                  # loop through all keys
    print(name, ":", contacts[name])


Example Run
1. Add Contact
2. View Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Exit

Choose: 1
Enter name: Arun
Enter phone number: 9876543210
Contact added!

Choose: 2
Enter name to view: Arun
Arun: 9876543210

Choose: 5
All Contacts:
Arun: 9876543210

Choose: 6
Goodbye!

Important things to handle
When viewing or updating or deleting a contact, check if name in contacts: first — otherwise trying to access or delete a name that doesn't exist will crash your program.
When adding, think about what should happen if the name already exists — should it silently overwrite, or warn the user first? Your choice, just be intentional about it.

Bonus (optional)
Add a Search option that finds contacts whose name contains a given substring (not just exact match) — hint: loop through contacts and use the in keyword on the name itself, e.g. if search_text in name:
