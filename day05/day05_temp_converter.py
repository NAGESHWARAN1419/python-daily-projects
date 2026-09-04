while True:
   value0 = input("Enter temperature value or (to quit press q):")
   if value0 == "q":
      print ()
      print ("====================================")
      print ()
      print ("Bye")
      print ()
      print ("====================================")
      break

   value = float (value0)

   unit = input ("Is this in Celsius or Fahrenheit? (C/F):")

   print ()
   print ("====================================")
   print ()
   if unit == "c" or unit == "C":
      f = (value * 9/5) + 32
      print (str(value)+"°C =",str(round(f,2))+"°F")
   elif unit == "f" or unit == "F":
      c = (value - 32) * 5/9
      print (str(value)+"°F =",str(round(c,2))+"°C")
   else:
      print ("Invaild input. You can choose c/f")

   print ()
   print ("====================================")
   print ()

