print ("-----------------------------------------------")
print ("Reverse a Number / Palindrome Number Checker")
print ("-----------------------------------------------")
while True:
   num0 = input("Enter a number:")
   if num0 == "q":
      print ()
      print ("========================================")
      print ()
      print ("Bye")
      print ()
      print ("========================================")
      break

   num = abs (int (num0))
   r_num = 0
   while num > 0:
      digit = num % 10
      r_num = r_num * 10 + digit
      num = num // 10
   print ()
   print ("========================================")
   print ()
   print (f"Reversed number: {r_num}")
   if r_num == abs(int(num0)):
     print (f"{r_num} Is a palindrome")
   else:
     print (f"{r_num} Is NOT a palindrome ")
   print ()
   print ("========================================")
   print ()
print ("-----------------------------------------------")
