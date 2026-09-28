while True:
   print ("1. Encode")
   print ("2. Decode")
   print ("3. Exit")
   opt0 = input("Choose: ")
   if opt0.lower() == "q":
      print ()
      print ("bye")
      print ()
      break
   opt = int(opt0)
   if opt == 1:
      print ()
      message = input("Enter message: ").lower()
      shift = int(input("Enter shift: "))
      result = ""
      for letter in message:
         if letter.isalpha():
            shifted = chr((ord(letter)-97+shift)%26+97)
            result += shifted
         else:
            result+=letter 
      print ()
      print ("Encoded:",result)
      print ()
   elif opt == 2:
      print ()
      message = input("Enter message: ").lower()
      shift = int(input("Enter shift: "))
      result = ""
      for letter in message:
         if letter.isalpha():
            shifted = chr((ord(letter)-97-shift)%26+97)
            result += shifted
         else:
            result+=letter 
      print ()
      print ("Decoded:",result)
      print ()
   elif opt == 3:
      print ()
      print ("Bye")
      print ()
      break
   else:
      print ()
      print ("Invalid option")
      print ()
