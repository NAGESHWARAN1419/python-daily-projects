amt = 5000
pin = 1234
attempt = 0
access_granted = False
while attempt < 3:
   pin0 =int (input("Enter your PIN: "))
   if pin0 == pin:
      access_granted = True
      break
   else:
      attempt += 1
      print (f"Wrong PIN. {3- attempt} attempts left.")
if not access_granted:
   print ("Too many wrong attempts. Card locked.")
else:


   while True:
      print ()
      print ("1.Check Balance")
      print ("2.Deposit")
      print ("3.Withdraw")
      print ("4.Exit")
      option0 = input ("Choose an option:")
      if option0 == "4":
         print ("Thank you for using the ATM.")
         print ()
         break
      option = int (option0)
      if option == 1:
         print (f"Current balance:{amt}")
         print ()
      elif option == 2:
         dp = abs (int (input ("Enter a deposit amount:")))
         amt = dp + amt
      elif option == 3:
         wd = int ( input ("Enter amount to withdraw:"))
         if wd > amt:
            print ("Insufficient funds!")
            print ()
         elif wd < 0:
            print ("Ivalid amount!")
         else:
            amt = amt - wd
            print (f"Withdrawal successful. New balance {amt}")
            print ()
      
