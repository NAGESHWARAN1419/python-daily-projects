print ("-----------------------------------------------------")
print ("Find Max, Min, and Average from a List of Numbers:- ")
print ("-----------------------------------------------------")
print ()
while True:
   text = input ("Enter numbers (comma-separated): ")
   if text == "q" or text == "Q":
      print ()
      print ("Bye")
      print ()
      break

   parts  = text .split(",")
   numbers = [int(x) for x in parts]

   manual_max = numbers[0]
   for num in numbers:
      if num > manual_max:
         manual_max = num

   manual_min = numbers[0]
   for num in numbers:
      if num < manual_min:
         manual_min = num

   sum_no = sum(numbers)

   average = round(sum(numbers) / len (numbers),2)

   print ()
   print ("-----------------------------------------------------")
   print ("Using built-in functions: ")
   print (f"Max: {max(numbers)}")
   print (f"Min: {min(numbers)}")
   print (f"Sum: {sum_no}")
   print (f"Average: {average}")
   print ()
   print ("Using manual loop:")
   print (f"Max: {manual_max}")
   print (f"Min: {manual_min}")
   print ("-----------------------------------------------------")
   print ()
