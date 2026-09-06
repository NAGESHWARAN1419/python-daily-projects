while True:
   print ("----------------------------------------------")
   print ("MULTIPLICATION TABLE GRENTERATOR")
   print ("----------------------------------------------")

   num0 = input("Enter a number or press q (quit): ")
   print ()
   if num0 == "q":
      print ()
      print ("==============================================")
      print ()
      print ("Bye")
      print ()
      print ("==============================================")
      print ("----------------------------------------------")
      break

   ran = int(input("Enter range value:"))
   num = int(num0)
   i = 1

   print ("==============================================")
   print ()
   for i in range (1,ran+1):
      print (num,"x",i,"=",num*i)

   print ()
   print ("==============================================")
   print ("----------------------------------------------")
   print ()
