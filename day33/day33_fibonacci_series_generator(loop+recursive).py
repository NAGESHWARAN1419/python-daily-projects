def fib_loop(n):
   series = []
   a = 0
   b = 1
   for i in range(n):
      series.append(a)
      a, b = b, a+b
   return series

def fib_recursive(n):
   if n == 1:
      return  0
   if n == 2:
      return 1
   return fib_recursive(n - 1) + fib_recursive(n - 2)

while True:
   n0 = input ("How many terms? ")
   if n0.lower() == "q":
      print ()
      print ("Bye")
      print ()
      break
   n = int (n0)
   if n <= 0:
      print ()
      print ("Please enter a number greater than 0.")
      print ()
      continue

   loop = fib_loop(n)
   recursive = fib_recursive(n)
   print ()
   print (f"Series (loop): {loop}")
   print (f"The {n} number (recursive): {recursive}")
   print ()
