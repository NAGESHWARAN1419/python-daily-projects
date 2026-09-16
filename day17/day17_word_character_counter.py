print ("=======================================================")
print ("Word/Character Counter in a Sentence")
print ("=======================================================")
print ()
while True:
   ste = input ("Enter a sentence: ")
   if ste =="q":
      print ()
      print ("=======================================================")
      print ()
      print ("Bye")
      print ()
      print ("=======================================================")
      print ()
      break

   ste1 = len(ste)
   ste2 = len (ste.replace (" ",""))
   ste3 = len(ste.split())
   print ()
   print ("-------------------------------------------------------")
   print (f"Character (with spaces): {ste1}")
   print (f"Character (without spaces): {ste2}")
   print (f"Words: {ste3}")
   v = 0
   for char in  ste:
      if char in  "aeiouAEIOU":
         v += 1
   print (f"Vowels: {v}")
   print ("-------------------------------------------------------")
   print ()
print ("=======================================================")
