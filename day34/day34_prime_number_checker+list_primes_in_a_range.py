
def is_prime(n):
   if n <2:
      return False 
   for i in range (2,n):
      if n % i ==0:
         return False
   return True

def primes_in_range(start,end):
   primes = []
   for num in range (start,end+1):
      if is_prime(num):
         primes.append(num)
   return primes

while True:
   print ("1. Check if a number is prime")
   print ("2. List all primes in a range")
   print ("3. Exit")
   opt = int (input ("Choose:"))
   if opt == 1:
      print ()
      n = int (input("Enter a number: "))
      result = is_prime(n)
      if result == True:
         print ()
         print (f"{n} is a prime number.")
      else:
         print ()
         print (f"{n} is NOT a prime number.")
      print ()
   elif opt ==2:
      print ()
      start = int (input("Enter start: "))
      end = int (input("Enter end: "))
      result = primes_in_range(start,end)
      if start > end:
         print ()
         print ("'Start' is greater than 'end'")
      elif result == []:
         print ()
         print ("No primes found.")
      else:
         print ()
         print (f"Primes between {start} to {end}: {result}")
      print ()
   elif opt ==3:
      print ()
      print ("Bye")
      print ()
      break
   else :
      print ()
      print ("Invaild option")
      print ()
      continue
