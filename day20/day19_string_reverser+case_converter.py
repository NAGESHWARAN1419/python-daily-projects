while True:
   ste = input ("Enter a string or (press q to Quit): ")
   if ste == "q" or ste == "Q":
      print ()
      print ("Bye")
      break
   print ("1. Reverse the string")
   print ("2. Convert to UPPERCASE")
   print ("3. Convert to lowercase")
   print ("4. Convert to Title Case")
   print ("5. Swap case (upper ↔ lower for each letter)")
   print ("6. Exit")
   opt = int ( input ("Choose: ") )
   if opt == 1:
      print ()
      ste0 = ste [::-1]
      print (ste0)
      print ()
   elif opt == 2:
      print ()
      ste0 = (ste).upper()
      print (ste0)
      print ()
   elif opt == 3:
      print ()
      ste0 = (ste).lower()
      print (ste0)
      print ()
   elif opt == 4:
      print ()
      ste0 = (ste).title()
      print (ste0)
      print ()
   elif opt == 5:
      print ()
      ste0 = (ste).swapcase()
      print (ste0)
      print ()
   elif opt == 6:
     print ()
     print ("Bye")
     break
   else: 
     print ()
     print ("Invaid option")
     break
   up_c = 0
   lw_c = 0
   for char in ste0:
      if char.isupper():
         up_c += 1
      elif char.islower():
         lw_c += 1
   print ("-------------------------------------")
   print (f"In the sentence: {ste0}")
   print (f"Uppercase letters: {up_c}")
   print (f"Lowercase letters: {lw_c}")
   print ("-------------------------------------")
   print ()
