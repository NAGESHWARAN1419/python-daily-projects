print ("==========================================================")
print ("------------------Simple Grading System-------------------")
print ("==========================================================")
print ()
while True:
   mark0 = input("Enter your marks or (press q to Quit) :")
   if mark0 == "q" or mark0 == "Q":
      print ()
      print ("==========================================================")
      print ()
      print ("-------------------------Bye------------------------------")
      print ()
      print ("==========================================================")
      print ()
      break

   mark = int (mark0)
   print ()
   print ("==========================================================")
   print ()
   if 100 < mark:
      print ("Invaild marks! Please enter a value between 0 to 100")
   elif mark >= 90:
      print ("Grade: A+")
   elif 80 <= mark < 90:
      print ("Grade: A")
   elif 70 <= mark < 80:
      print ("Grade: B")
   elif 60 <= mark < 70:
      print ("Grade: C")
   elif 40 <= mark < 60:
      print ("Grade: D")
   elif 0 <= mark < 40 :
      print ("Fail")
   elif mark < 0:
     print ("Invaild mark")

   print ()
   print ("==========================================================")
   print ()

print ("==========================================================")
