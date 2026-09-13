print ("=======================================================")
print ("==========Pattern Printing (Stars/Pyramid)=============")
print ("=======================================================")
while  True:
   print ()
   n0 = input("Enter the number of row or (press q to quit):")
   if n0 == "q":
      print ()
      print ("=======================================================")
      print ()
      print ("-------------------------Bye---------------------------")
      print ()
      print ("=======================================================")
      print ()
      break

   n = int(n0)

   patten = int(input("Which patten did you need press(1 or 2):"))
   if patten == 1:
      for i in range (1,n+1):
         for j in range (i):
            print ("*",end="")
         print ()
      print ("__________________________________________________")
   elif patten == 2:
      for i in range (1,n+1):
         spaces = n - i
         stars =2*i - 1
         print (" " * spaces + "*" * stars)
      print ("__________________________________________________")
print ("=======================================================")
