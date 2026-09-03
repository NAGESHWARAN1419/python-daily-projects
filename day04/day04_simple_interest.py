while True:
   p0 = input("Enter Pricnipal amount or press q to quit:")

   if p0 == "q":
      print ()
      print ("===============")
      print ("Bye")
      print ("===============")
      break

   r = float(input("Enter Rate of interest(%):"))
   t = float(input("Enter Time peroid(years):"))

   p = float(p0)

   si = (p*r*t)/100

   total_amt = p+si

   print ()
   print ("===================================")
   print ()
   print ("Simple Interest = ",round(si,2))
   print ("Total Amount = ",round(total_amt,2))
   print ()
   print ("===================================")
   print ()


