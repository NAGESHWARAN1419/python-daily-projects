while True:
   num_input = input("Enter a number or q-quite: ")
   print ()

   if num_input =="q":
      print ("===============================")
      print ()
      print ("Bye")
      print ()
      print ("===============================")
      break

   num = int(num_input)

   print ("===============================")
   print ()

   if num%2 == 0:
      print (num,"is Even")
      a = "Even"
   else:
      print (num,"is Odd")
      a = "Odd"

   if num<0:
      print (num,"is negative")
      b = "negative"
   elif num>0:
      print (num,"is positive")
      b = "positive"
   else:
      print (num,"is zero")
      b = "zero"
   print ("-----------------------------")
   print (num,"is",a,"and",b)
   print ("-----------------------------")
   print ()
   print ("===============================")
   print ()
