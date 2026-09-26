item ={}
while True:
   print ("1. Add New Item")
   print ("2. Restock Item (increase quantity)")
   print ("3. Sell Item (decrease quantity)")
   print ("4. View Inventory")
   print ("5. Low Stock Alert (items with quantity < 5)")
   print ("6. Exit")
   opt = int (input("Choose: "))
   if opt == 1:
      print ()
      print ("Add New Item:- ")
      name = input ("Enter item name: ").title()
      if name in item:
         print (f"'{name}' already exists! Use Restock instead.")
      else:
         qty = int (input("Enter starting quantity: "))
         item[name] = qty
         print ()
         print ("Item added!")
      print ()
   elif opt == 2:
      print ()
      name = input ("Enter item name: ").title()
      if name in item:
         qty0 = int (input("Enter Adding quantity: "))
         item[name] +=qty0
         print ()
         print ("Item added successful!")
      else :
         print ()
         print ("Invalid name!")
      print ()
   elif opt == 3:
      print ()
      name = input ("Enter item name: ").title()
      if name in item:
         qty0 = int (input("Enter selling quantity: "))
         if qty0 <= item[name]:
            item[name] -=qty0
            print ()
            print ("Item selled successful!")
         else:
            print (f"Not enough stock! Only {item[name]} available.") 
      else :
         print ()
         print ("Invalid name!")
      print ()
   elif opt == 4:
      print ()
      print ("Viewing Inventory:-")
      for index,n  in enumerate (item,start=1):
         print (f"{index}) {n} : {item[n]}")
      print ()
   elif opt == 5:
      print ()
      print ("Low Stock:- ")
      found_low = False
      for n in item:
         if item[n] < 5:
           print (n,":",item[n])
           found_low = True
      if not found_low:
         print ()
         print (" All items are above than 5 in stock")
      print ()
   elif opt == 6:
      print ()
      print ("Bye")
      print ()
      break
