address_book = {
    "arun": {"phone": "9876543210", "email": "arun@gmail.com", "city": "chennai"},
    "priya": {"phone": "9123456780", "email": "priya@gmail.com", "city": "madurai"}
}
print ()
while True:
   print ("Menu:")
   print ("1. Add Contact")
   print ("2. Search Contact")
   print ("3. Update Contact")
   print ("4. Delete Contact")
   print ("5. View All Contacts")
   print ("6. Exit")
   opt = int (input ("Choose: "))
   if opt == 1:
      print ()
      name =input("Enter name: ").lower()
      if name in address_book:
         print ("name is exits.")
      else:
         print ()
         phone = input("Enter phone: ")
         email = input("Enter email: ").lower()
         city = input ("Enter city: ").lower()
         address_book[name]={"phone": phone,"email": email,"city": city}
         print ()
         print ("Detail added!")
      print ()

   elif opt == 2:
      print ()
      search_type = input("Search by name or city: ").lower()
      search_text = input("Enter search text: ").lower()
      print ()
      found = False
      if search_type == "name":
         for name in address_book:
            if search_text in name:
               print (name.title())
               print (" Phone:", address_book[name]["phone"])
               print (" Email:", address_book[name]["email"])
               print (" City:", address_book[name]["city"])
               print ()
               found = True
      elif search_type == "city":
         for name in address_book:
            if search_text in address_book[name]["city"]:
               print (name.title())
               print (" Phone:", address_book[name]["phone"])
               print (" Email:", address_book[name]["email"])
               print (" City:", address_book[name]["city"])
               print ()
               found = True

      else:
         print ("Invalid search type.")
      if not found:
         print ("No matching contacts found")
      print ()

   elif opt == 3:
      print ()
      name = input("Enter the name to update: ").lower()
      if name in address_book:
         field = input ("Which field? (phone/email/city): ").lower()
         if field in ["phone","email","city"]:
            new_value = input(f"Enter new {field}: ").lower()
            address_book[name][field] = new_value
            print ()
            print ("Contact update!")
         else:
            print ()
            print ("Invalid field name.")
      else:
         print ("Name not found.")
      print ()

   elif opt == 4:
      print ()
      delete_name =input("Enter delete address name: ").lower()
      print ()
      if delete_name in address_book:
        conform = input (f"Are you sure you want to delete {delete_name}? (y/n): ").lower() 
        if conform == "y":
           print ()
           print (f"{delete_name} Deleted Successfully!")
           del address_book[delete_name]
        else:
           print ("Delete cancelled.")
      else :
         print ("Name not found.")
      print ()

   elif opt == 5:
      print ()
      for name in address_book:
         print (name.title())
         print (" Phone:", address_book[name]["phone"])
         print (" Email:", address_book[name]["email"])
         print (" City:", address_book[name]["city"])
         print ()

   elif opt == 6:
      print ()
      print ("Bye")
      print ()
      break
