while True:
   print ("--------------------------------------")
   print ("Sum of Digits of a Number:-")
   print ("--------------------------------------")
   print ()
   num0 = input("Enter a number or press q to Quit:")
   if num0 == "q":
      print ()
      print ("======================================")
      print ()
      print ("Bye")
      print ()
      print ("======================================")
      break

   num = abs (int (num0))
   total = 0

   while num > 0:
      digit = num % 10
      total = total + digit
      num = num // 10
   print ()
   print ("======================================")
   print ()
   print (f"Sum of digit = {total}")
   print ()
   print ("======================================")
   print ()
