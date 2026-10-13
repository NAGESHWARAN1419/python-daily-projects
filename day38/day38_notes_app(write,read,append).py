while True:
   print ("1. Write New Notes (replaces everything)")
   print ("2. Add a Note")
   print ("3. Read Notes")
   print ("4. Exit")
   print ("5. Delete a Note")
   opt0 = input("Choose: ").strip(" ")
   opt =int(opt0)
   try:
      if opt == 1:
         print ()
         notes = input("Enter your note: ").title()
         print ()
         if len(notes.strip(" ")) == 0:
            print ("No notes yet.")
         else:
            ask = input ("Are you sure it erases all (y/n): ")
            if ask.lower() == "y":
               with open ("notes.txt","w") as file:
                  file.write(f"{notes}\n")
               print ("New Note added!")
            elif ask.lower() == "n":
               print ("file not chage")
            else:
               print ("Press 'y' for Yes and 'n' for NO")
         print ()

      elif opt == 2:
         print ()
         notes = input("Enter your note: ").title()
         if len(notes.strip(" ")) == 0:
            print ("No notes yet.")
         else:
            with open ("notes.txt","a") as file:
               file.write(f"{notes}\n")
            print ("Note added!")

         print ()

      elif opt == 3:
         print ()
         print ("Your Notes:-")
         with open("notes.txt","r") as file:
            notes = file.readlines()
         if len (notes) == 0:
            print ("No notes yet.")
         else:
            line = 0
            for number , note in enumerate(notes, start=1):
               print (f"{number}. {note.strip()}")
               line += 1
            print ()
            print (f"Total lines {line}")
         print ()

      elif opt == 4:
         print ()
         print ("Bye")
         print ()
         break

      elif opt == 5:
         print ()
         with open("notes.txt","r") as file:
            notes = file.readlines()
         if len(notes) == 0:
            print ("No notes yet.")
         else:
            for number, note in enumerate(notes, start=1):
               print (f"{number}. {note.strip()}")
            num = int(input("Enter note number to delete: "))
            if 1 <= num <= len(notes):
               removed = notes.pop(num - 1)
               with open("notes.txt","w") as file:
                  file.writelines(notes)
               print (f"Deleted: {removed.strip()}")
            else:
               print ("Invalid note number.")
         print ()

      else:
         print ()
         print ("Invaild option")
         print ()
         continue

   except FileNotFoundError:
      print ()
      print ("File Not Found Error. make a 'notes.txt' file in the same folder")
      print ()
      continue
