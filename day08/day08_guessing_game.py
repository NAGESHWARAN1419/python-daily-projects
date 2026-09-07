import random
while True:
   num = random.randint(1,100)
   attempt = 0

   while True:
      print ()
      print ("Guess the number from 1 to 100")
      print ("______________________________________________")
      print ()
      print ("I'm thinking of a number between 1 to 100.")
      gues = input ("Enter your guess:")
      if gues == "q":
         print ()
         break

      guess = int (gues)
      attempt += 1

      if guess < num:
         print ("Too low!")
      elif guess > num:
         print ("Too high!")
      else:
         print (f"Correct! Your guessed it in {attempt} attempts.")
         print ()
         break

      if attempt < 7 :
         print ()
         print ("----------------------------------")
         print (f"You have only {7-attempt} attempts")
         print ("----------------------------------")
      else:
         print ("+++++++++++++++++++++++++++++++++++++++++++")
         print ()
         print ("Game over")
         print ()
         print ("+++++++++++++++++++++++++++++++++++++++++++")
         print ()
         break

   play = input ("If you want to play again(y/n):")
   if play == "y" or play == "Y":
      print ("==============================================")
      print ()
      print ("~ ok lets play again! ~")
      print ()
      print ("==============================================")
      continue
   elif play == "n" or play == "N":
      print ()
      print ("==============================================")
      print ()
      print ("Bye")
      print ()
      print ("==============================================")
      print ("______________________________________________")
      break
