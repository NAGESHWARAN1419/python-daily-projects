def factorial_loop(n):
   result=1
   for i in range (1,n+1):
      result=result*i
   return result

def factorial_recursion(n):
   if n== 0 or n == 1:
      return 1
   return n * factorial_recursion(n-1)
while True:
   n0 = input("Enter a number: ")
   if n0 == "q":
      print ()
      print ("Bye")
      print ()
      break
   n = int (n0)
   if n < 0:
      print ()
      print ("Factorial is not defined for negative numbers.")
      print ()
      continue

   loop = factorial_loop(n)
   recursion = factorial_recursion(n)
   print ()
   print (f"Using loop: {n}! = {loop}")
   print (f"Using recursion: {n}! ={recursion}")
   print ()
   print ()
