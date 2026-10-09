def add(first,second):
  return first+second

def sub(first,second):
  return first-second

def mult(first,second):
  return first*second

def div(first,second):
  if second ==0:
    return "Cannot divide by zero"
  return first/second

def power(first,second):
  return first**second

def modules(first,second):
  if second ==0:
    return "Cannot calculate modulus by zero"
  return first%second

while True:
   first = float(input("Enter first number: "))
   second = float (input("Enter second number: "))
   opt = input("Choose operation(+,-,*,/,**,%) or 'q' to quit: ")
   if opt == "q" or opt == "Q":
      print ()
      print ("Bye")
      print ()
      break

   elif opt == "+":
      result = add(first,second)

   elif opt == "-":
      result = sub(first,second)

   elif opt == "*":
      result = mult(first,second)

   elif opt == "/":
      result = div(first,second)

   elif opt == "**":
      result = power(first,second)

   elif opt.lower() == "%":
      result = modules(first,second)

   else:
      print ()
      print (f"'{opt}' Invaild Input")
      print ()
      continue

   print ()
   print (f"Result: {first} {opt} {second} = {result}")
   print ()

