print ("=====================================================")
print ("Palindrome String Checker")
print ("=====================================================")
while True:
   wrd0 = input ("Enter a word or (press q to Quite): ")
   wrd1 = wrd0.lower()
   wrd = wrd1.replace(" ","")
   r_wrd = wrd [::-1]
   if  wrd == "q":
      print ()
      print ("=====================================================")
      print ()
      print ("Bye")
      print ()
      print ("=====================================================")
      print ()
      break

   if wrd == "":
      print ("Please enter an actual word or phrase")
      print ()
   elif wrd == r_wrd:
      print (f"{wrd0} is a palindrome.")
      print ()
   else:
      print (f"{wrd0} is NOT a palindrome.")
      print ()
print ("=====================================================")
