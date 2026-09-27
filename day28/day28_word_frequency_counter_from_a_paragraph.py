
while True:
   para = input("Enter a paragraph: ").lower()
   if para == "q":
      print ()
      print ("Bye")
      print ()
      break

   
   words = para.split(" ")
   word_count = {}
   for w in words:
      word = w.strip(".,?!")
      word_count[word] = word_count.get(word,0)+1

   print ()
   for word in word_count:
      print (f"{word}:{word_count[word]}")
   print ()
