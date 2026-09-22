cart = []
while True:
   print ("------------------------------------------------------")
   print ("1. Add Item")
   print ("2. View Cart")
   print ("3. Remove Item")
   print ("4. Total Bill")
   print ("5. Exit")
   print ("------------------------------------------------------")
   opt = int ( input ("Choose:"))
   if opt ==1:
      name = input ("Enter item name: ").title()
      found = False
      for n,p,q in cart:
         if n == name:
            found = True
      if found:
         qty = int(input(f"Enter addtional quantity of {name}: "))
         new_cart = []
         for n,p,q in cart:
            if n == name:
               new_cart.append((n,p,q+qty))
            else:
               new_cart.append((n,p,q))
         cart = new_cart 
      else:
         price = int(input("Enter price: "))
         quantity = int(input("Enter quantity: "))
         cart.append((name,price,quantity))
      print ()
      print ("------------------------------------------------------")
      print ("Item added!")
      print ("------------------------------------------------------")
      print ()

   elif opt ==2:
      print ()
      print ("------------------------------------------------------")
      print ("Your Cart:")
      grant_total =0
      for  name,price,quantity in cart:
         total = price*quantity
         grant_total += total
         print (f"{name} - ₹{price} x {quantity} = ₹{total}")
      print ("------------------------------------------------------")
      print ()

   elif opt ==3:
      print ()
      print ("Your Cart Items:")
      for  name,price,quantity in cart:
          item = name,price,quantity
          print (name)
      print ()
      remove_item = input("Enter item name to remove: ").title()
      new_cart = []
      found = False
      for name, price, quantity in cart:
         if name == remove_item:
            found = True
         else:
            new_cart.append((name,price,quantity))
      cart = new_cart
      print ()
      print ("------------------------------------------------------")
      if found:
         print ("Item removed!")
      else:
         print ("Item not found in cart.")
      print ("------------------------------------------------------")
      print ()

   elif opt ==4:
      print ()
      print ("------------------------------------------------------")
      grant_total = 0
      for  name,price,quantity in cart:
         total = price*quantity
         grant_total += total
         print (f"{name} - ₹{price} x {quantity} = ₹{total}")
      print (f"Total Bill: ₹{grant_total}")
      print ("------------------------------------------------------")
      print ()

   elif opt ==5:
      print ()
      print ("------------------------------------------------------")
      print ("Bye")
      print ("------------------------------------------------------")
      print ()
      print ("------------------------------------------------------")
      break
