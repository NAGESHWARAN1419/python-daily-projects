print ()
print ("Password Strength Checker:-")
print ()
import getpass
def check_password(password):
   has_upper=False
   has_lower=False
   has_digit=False
   has_special=False
   specials = "!@#$%^&*()_+-=?"
   for char in password:
      if char.isupper():
         has_upper = True
      elif char.islower():
         has_lower = True
      elif char.isdigit():
         has_digit = True
      elif char in specials:
         has_special = True
   score = 0
   tips = []
   if len(password)>=8:
      score += 1
   else:
      tips.append("Use at least 8 characters")
   if has_upper:
      score +=1
   else:
      tips.append ("Add an uppercase letter")
   if has_lower:
      score +=1
   else:
      tips.append ("Add a lowercase letter")
   if has_digit:
      score +=1
   else: 
      tips.append ("Add a digit")
   if has_special:
      score +=1
   else:
      tips.append("Add a special character")
   return score, tips

while True:
   password = getpass.getpass ("Enter a password (or q to quit): ")
   if password == "q" or password == "Q":
      print ()
      print ("Bye")
      print ()
      break
   if password == " "or password =="":
      print ()
      print ("Password cannot be empty.")
      print ()
      continue

   score, tips = check_password(password)
   if score <=2:
      strength = "Weak"
   elif score <=4:
      strength = "Medium"
   else:
      strength = "Strong"

   print ()
   print ("------------------------------------------------")
   print (f"Strength: {strength} (score {score}/5)")
   print ("------------------------------------------------")
   print ()
   if len (tips) > 0:
      print ("Tips to improve:")
      for tip in tips:
         print ("--",tip)
   print ()
   print ("------------------------------------------------")
   print ()

