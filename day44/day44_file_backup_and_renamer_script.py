import os
import shutil
def get_files (folder):
   names = sorted(os.listdir(folder))
   files =[]
   for name in names:
      if os.path.isfile(os.path.join(folder, name)):
         files.append(name)
   return files
while True:
   print ("1. List files in a folder")
   print ("2. Backup a folder")
   print ("3. Rename files in a folder")
   print ("4. Exit")
   try:
      opt = int(input("Choose: "))
   except ValueError:
      print()
      print("Please enter a number.")
      print()
      continue
   if opt ==1:
      print ()
      folder = input ("Enter folder name: ").strip().rstrip("/")
      if not os.path.isdir(folder):
         print ("Folder not found.")
      else:
         files = get_files(folder)
         if len(files) == 0:
            print ("No files found.")
         else:
            for number,name in enumerate(files, start=1):
                print (f"{number}. {name}") 
      print ()
   elif opt ==2:
      print ()
      folder = input("Enter folder name: ").strip().rstrip("/")
      if not os.path.isdir(folder):
         print ("Folder not found.")
      else:
         files =get_files(folder)
         if len(files) ==0:
            print ("No file found.")
         else:
            backup_folder =folder + "_backup"
            os.makedirs(backup_folder, exist_ok=True)
            for name in files:
               source = os.path.join(folder, name)
               destination = os.path.join(backup_folder, name)
               shutil.copy(source, destination)
            print (f"{len(files)} files coped to {backup_folder}")
      print ()
   elif opt == 3:
      print()
      folder = input("Enter folder name: ").strip().rstrip("/")
      if not os.path.isdir(folder):
         print("Folder not found.")
      else:
         files = get_files(folder)
         prefix = input("Enter new name prefix: ").strip()
         if len(files) == 0:
            print("No files found.")
         elif prefix == "":
            print("Prefix cannot be empty.")
         else:
            confirm = input(f"Rename {len(files)} files? (y/n): ").lower()
            if confirm == "y":
               count = 1
               for name in files:
                  extension = os.path.splitext(name)[1]
                  new_name = f"{prefix}_{count}{extension}"
                  old_path = os.path.join(folder, name)
                  new_path = os.path.join(folder, new_name)
                  if os.path.exists(new_path):
                     print(f"Skipped {name}: {new_name} already exists")
                  else:
                     os.rename(old_path, new_path)
                     print(f"{name} -> {new_name}")
                  count += 1
               if len(renamed)>0:
                  last_folder = folder
                  last_renames = renamed
               print (f"{len(renamed)} files renamed.")
            else:
               print("Rename cancelled.")
      print ()
   elif opt ==4:
      print ()
      if len(last_renames) == 0:
         print ("Nothing to undo.")
      elif not os.path.isdir(last_folder):
         print ("The folder no longer exists.")
      else:
         confirm = input (f"Undo {len(last_rename)} renames in {last_folder}? (y/n): ").lower()
         if confirm == "y":
            undone = 0
            for old_name, new_namein last_renames:
               old_path = os.path.join(last_folder, old_name)
               new_path = os.path.join(last_folder, new_name)
               if not os.path.exists(new_path):
                  print (f"Skipped {new_name}: file not found")
               elif os.path.exists(old_path):
                  print (f"Skipped {new_name}: {old_name} already exists")
               else:
                  os.rename(new_path, old_path)
                  print (f"{new_name} -> {old_name}")
                  undone += 1
            print (f"{undone} files restored.")
            last_rename = []
         else:
            print ("Undo cancelled.")
      print ()
   elif opt ==5:
      print ()
      print ("Bye")
      print ()
      break
   else:
      print ()
      print ("Invalid operation.")
      print ()
      continue
