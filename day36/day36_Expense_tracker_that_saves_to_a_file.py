while True:
   print ("1. Add Expense")
   print ("2. View All Expense")
   print ("3. Total Spent")
   print ("4. Exit")
   opt = int(input("Choose: "))
   if opt ==1:
      print ()
      description = input("Enter description: ").replace(","," ")
      amount = float(input("Enter amount: "))
      if amount < 0:
         print ("Amount cannot be negative.")
      else:
         with open ("expenses.txt","a")as file:
            file.write(f"{description}, {amount}\n")
         print ("Expenses saved!")
      print ()
   elif opt ==2:
      print ()
      try :
         with open("expenses.txt","r")as file:
            number = 1
            for line in file:
               description, amount = line.strip().split(",")
               print (f"{number}.{description.title()} -₹{float(amount)}")
               number +=1
      except FileNotFoundError:
         print ("No expenses yet.")
      print ()
   elif opt ==3:
      print ()
      total = 0
      try:
         with open("expenses.txt","r")as file:
            for line in file:
               description, amount = line.strip().split(",")
               total += float(amount)
         print (f"Total spent: ₹{total}")
      except FileNotFoundError:
         print ("No expenses yet.")
      print ()
   elif opt ==4:
      print ()
      print ("Bye")
      print ()
      break
   else:
      print ()
      print ("Invaid operation")
      print ()
      continue
