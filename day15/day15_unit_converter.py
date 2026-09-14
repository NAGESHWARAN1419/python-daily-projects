while True:
   print ()
   print ("1.Lenght Converter")
   print ("2.Weight Converter")
   print ("3.Temperature Converter")
   print ("4.Exit")
   opt0 = int ( input ("Choose:"))
   if opt0 == 1:
      while True:
         print ()
         print ("1.Km to Miles")
         print ("2.Miles to Km")
         print ("3.Back to Menu")
         opt1 = int (input ("Choose:"))
         if opt1 == 1:
            km = float ( input ("Enter Km:"))
            m = round (km * 0.621371,2)
            print (f"{km} km = {m} miles")
            print ()
         elif opt1 == 2:
            m = float ( input ("Enter Miles:"))
            km = round (m / 0.621371,2)
            print (f"{m} miles = {km} km")
            print ()
         elif opt1 == 3:
            break
         else :
            print ("Invalid operation")
            print ("Press 3 to back to menu")
            print ()
   elif opt0 == 2:
      while True:
         print ()
         print ("1.Kilogram to pounds")
         print ("2.Pounds to Kilogram")
         print ("3.Back to Menu")
         opt1 = int (input ("Choose:"))
         if opt1 == 1:
            kg = float ( input ("Enter Kilogram:"))
            lb = round (kg * 2.20462,2)
            print (f"{kg} kilogram = {lb} lb")
            print ()
         elif opt1 == 2:
            lb = float ( input ("Enter Pounds:"))
            kg = round (lb / 2.20462,2)
            print (f"{lb} lb = {kg} kilogram")
            print ()
         elif opt1 == 3:
            break
         else :
            print ("Invalid operation")
            print ("Press 3 to back to menu")
            print ()
   elif opt0 == 3:
      while True:
         print ()
         print ("1.Celsius to Fahrenheit")
         print ("2.Fahrenheit to Celsius")
         print ("3.Back to Menu")
         opt1 = int (input ("Choose:"))
         if opt1 == 1:
            c = float ( input ("Enter Celsius:"))
            f = round ((c * 9/5)+32 ,2)
            print (f"{c}°C = {f}°F")
            print ()
         elif opt1 == 2:
            f = float ( input ("Enter Fahrenheit:"))
            c = round ((f - 32) * 5/9 ,2)
            print (f"{f}°F = {c}°C")
            print ()
         elif opt1 == 3:
            break
         else :
            print ("Invalid operation")
            print ("Press 3 to back to menu")
            print ()
   elif opt0 == 4:
      print ()
      print ("=====================================")
      print ()
      print ("Bye")
      print ()
      print ("=====================================")
      print ()
      break
