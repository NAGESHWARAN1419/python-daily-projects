history =[]
attempts = 0
while True:
   while True:
      first_number0 = input("Enter first number (q = quit, h = history): ")
      if first_number0.lower() == "q":
         print ()
         print ("Bye")
         print ()
         quit()
      if first_number0.lower() == "h":
         print ()
         if len(history) == 0:
            print ("No calculations yet.")
         else:
            for number, entry in enumerate(history, start=1):
               print (f"{number}. {entry}")
         print (f"Attempts so far: {attempts}")
         print ()
         continue
      try:
         first_number = float(first_number0)
         break
      except ValueError:
         print ()
         print ("That is not a valid number. Try again.")
         print ()
   try:
      second_number = float(input("Enter second number: "))
      opt = input("Choose operation (+, -, *, /, **, %): ")
      if opt =="+":
         print ()
         result = first_number + second_number
         print ()
      elif opt =="-":
         print ()
         result = first_number - second_number
         print ()
      elif opt =="*":
         print ()
         result = first_number * second_number
         print ()
      elif opt =="/":
         print ()
         result = first_number / second_number
         print ()
      elif opt =="**":
         print ()
         result = first_number ** second_number
         print ()
      elif opt =="%":
         print ()
         result = first_number % second_number
         print ()
      else:
         print ()
         print ("Invalid operation.")
         print ()
         continue
   except ValueError:
      print ("That is not a valid number. Try again.")
      print ()
   except ZeroDivisionError:
      print ("Error: cannot divide by zero.")
      print ()
   except OverflowError:
      print ("Error: the result is too large.")
      print ()
   else:
      line = f"{first_number} {opt} {second_number} = {result}"
      print (f"Result: {line}")
      history.append(line)
      print ()
   finally:
      attempts += 1
