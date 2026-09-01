while True:
   first_number = (float(input("Enter first number:")))
   second_number = (float(input("Enter second number:")))
   operation = input("Choose operation(+,-,*,/)or use 'q'-Quit:")
   
   if operation =="q":
      print ()
      print ("Bye")
      break
   print ("=======================================================================")
   print ()
   try:
      if operation == "+":
         print ("Result:",first_number,"+",second_number,"=",first_number+second_number)
      elif operation == "-":
         print ("Result:",first_number,"-",second_number,"=",first_number-second_number)
      elif operation == "*":
         print ("Result:",first_number,"*",second_number,"=",first_number*second_number)
      elif operation == "/":
         print ("Result:",first_number,"/",second_number,"=",first_number/second_number)
      else:
         print ("Invaild operation")

   except ZeroDivisionError:
      print ("Cannot divide by zero")
   print ()
   print ("=======================================================================")

