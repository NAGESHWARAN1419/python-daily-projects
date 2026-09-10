print ()
print ("--------------------------------------------------")
print ("Leap Year Calculater:-")
print ("--------------------------------------------------")
while True:
   year0 = input ("Enter a year or press q to quit:")
   print ()
   print ("============================================")
   print ()
   if year0 == "q":
      print ("Bye")
      print ()
      print ("============================================")
      break

   year = int (year0)

   if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      print (f"{year} is a leap year.")
   else:
      print (f"{year} is NOT a leap year.")
   print ()
   print ("============================================")

print ("--------------------------------------------------")

