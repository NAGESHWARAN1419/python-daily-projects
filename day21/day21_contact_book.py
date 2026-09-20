contact_book ={}
while True :
   print ("1. Add Contact")
   print ("2. View Contact")
   print ("3. Update Contact")
   print ("4. Delete Contact")
   print ("5. View All Contacts")
   print ("6. Search Contacts")
   print ("7. Exit")
   opt = int ( input ("Choose:") )
   if opt ==1:
      name = input ("Enter name:").title()
      number = int(input(f"Enter {name} number:"))
      contact_book[name]= number
      print ()
      print (f"{name} Contact added successfully!")
      print ()

   elif opt ==2:
      name0 = input ("Enter name to view:").title()
      print ()
      if name0 in contact_book:
         print (f"{name0} Founded!")
         print (name0, ":", contact_book[name0])
      else:
         print ("Invalid name")
      print ()

   elif opt ==3:
      name0 = input ("Enter update person name:").title()
      new_number = int (input(f"Enter {name0} updated number:"))
      print ()
      if name0 in contact_book:
         contact_book[name0]= new_number
         print ("Successfully updated!")
      else:
         print ("Invalid name")
      print ()

   elif opt ==4:
      name0 = input ("Enter delete contact name:").title()
      print ()
      if name0 in contact_book:
         print (f"{name0} Deleted successfully")
         del contact_book[name0]
      else:
         print ("Invalid name")
      print ()

   elif opt ==5:
      print ()
      print ("All Contacts:")
      for name in contact_book:
         print (name ,":", contact_book[name])
      print ()

   elif opt == 6:
      search_text = input("Enter name to search: ").lower()
      print()
      found = False
      for name in contact_book:
         if search_text in name.lower():
             print(name, ":", contact_book[name])
             found = True
      if not found:
         print("No matching contacts found")
      print()

   elif opt ==7:
      print ()
      print ("Goodbye!")
      print ()
      break

   else:
      print ()
      print ("Invalid option")
      print ()
