import getpass
def load_users():
   users = {}
   try :
      with open("users.txt","r")as file:
         for line in file:
            username,password =line.strip("\n").split(",",1)
            users[username] = password
   except FileNotFoundError:
      pass 
   return users
def save_users(users):
   with open ("users.txt","w")as file:
      for username in users:
         file.write(f"{username},{users[username]}\n")
users = load_users()
def login(username):
   for attempt in range(3):
      password = getpass.getpass("Enter password: ")   
      if users[username] == password:
         return True
      print (f"Wrong password. {2-attempt} attempts left.")
   return False
locked =[]
while True:
   print ("1.Register")
   print ("2.Login")
   print ("3.Exit")
   try:
      opt = int (input("Choose: "))
   except ValueError:
      print ()
      print ("PLease enter a number.")
      print ()
      continue
   if opt == 1:
      print ()
      username = input ("Enter username: ").title().replace(" ","")
      if username == "":
         print ()
         print ("Username cannot be empty.")
         print ()
      elif "," in username:
         print ()
         print ("Username cannot contain a comma.")
         print ()
      elif username in  users:
         print ()
         print ("Username already exits.")
         print ()
      else:
         password = getpass.getpass("Enter password: ")
         if len(password) < 6:
           print () 
           print ("Password must be at least 6 characters.")
         else :
            users[username] = password
            save_users(users)
            print ("Registered successfully!")
      print ()
   elif opt ==2:
      print ()
      username = input ("Enter username: ").title().replace(" ","")
      if username not in users:
         print ()
         print ("User not found.")
      elif username in locked:
         print ()
         print ("This account is locked for this session.")
      else:
         if login(username):
            print ()
            print (f"Login successful.Welcome, {username}!")
         else:
            locked.append(username)
            print ()
            print ("Account locked.")
      print ()
   elif opt ==3:
      print ()
      print ("Bye")
      print ()
      break
   else:
      print ()
      print ("Invalid operation")
      print ()
      continue
