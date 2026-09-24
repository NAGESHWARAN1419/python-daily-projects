while True:
   text = input("Enter numbers (comma-separated like 1,2,2,3, etc..): ")
   if text == "q" or text == "Q":
       print ()
       print ("Bye")
       print ()
       break

   parts = text.split(",")
   numbers = [int(x) for x in parts]

   unique_manual = []
   for num in numbers:
      if num not in unique_manual:
         unique_manual.append(num)

   unique_set = list(set(numbers))

   print (f"Method 1 (manual): {unique_manual}")
   print (f"Method 2 (using set): {unique_set}")
   print ()
