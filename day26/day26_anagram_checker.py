while True:
   first_word = input ("Enter first word: ").lower()
   if first_word == "q":
      print ()
      print ("Bye")
      print ()
      break
   second_word = input ("Enter second word: ").lower()
   if second_word == "q":
      print ()
      print ("Bye")
      print ()
      break

   print ()
   if sorted(first_word) == sorted(second_word):
      print (f"'{first_word}' and '{second_word}' are anagrams!")

   else:
      print (f"'{first_word}' and '{second_word}' are  NOT anagrams!")
   print ()
 
