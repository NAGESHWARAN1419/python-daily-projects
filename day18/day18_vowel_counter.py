print ("===================================================")
print ("Vowel Counter in a String")
print ("===================================================")
while True :
   ste = input ("Enter a sentence or (press q in Quit):").lower()
   if  ste == "q":
      print ()
      print ("===================================================")
      print ()
      print ("Bye")
      print ()
      print ("===================================================")
      print ()
      break

   v_c =  {"a":0,"e":0,"i":0,"o":0,"u":0}
   for char in ste:
      if char in v_c:
         v_c[char] += 1
   for key in v_c:
     print (f"{key}:{v_c[key]}")
   print ()
print ("===================================================")
