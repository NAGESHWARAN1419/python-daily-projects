import random
questions = [
      {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "B"
      },
      {
        "question": "What does len('hello') return?",
        "options": ["4", "5", "6", "Error"],
        "answer": "B"
      },
      {
        "question": "Which of the following built-in Python data types is immutable, meaning its values cannot be modified after creation?",
        "options": ["Tuple","List","Set","Dictionary"],
        "answer": "A"
      },
      {
        "question": "num1 = 5; num2 = 10; total = num1 + num2. What is total?",
        "options": ["25","5","15","10"],
        "answer": "C"
      },
      {
        "question": "num = 7 what is (num % 2) ?",
        "options": ["2","7","0","1"],
        "answer": "D"
      },
]
def play_quiz():
   name = input("Enter your name: ").strip().replace(","," ").title()
   if name == "":
      print ("Name cannot be empty.")
      return
   random.shuffle(questions)
   score = 0
   letters = "ABCD"
   for number, q in enumerate (questions, start=1):
      print ()
      print (f"Question: {number}: {q['question']}")
      for index, option in enumerate (q["options"]):
         print (f"{letters[index]}. {option}")
      while True:
         answer = input("Your answer (A/B/C/D): ").strip().upper()
         if answer in ["A","B","C","D"]:
            break
         print ("Please type A, B, C or D.")
      if answer == q ["answer"]:
         print ("Correct!")
         score += 1
      else:
         print (f"Wrong! The correct answer is {q['answer']}.")
   print ()
   print (f"{name}, you scored {score} out of {len(questions)}.")
   with open  ("scores.txt","a") as file :
      file.write(f"{name}, {score},{len(questions)}\n")
   print ("Score saved!")
   percent = round(score / len(questions) * 100, 1)
   print (f"Percentage: {percent}%")
   if score == len(questions):
      print ("Perfect")
   elif score >= 3:
      print ("Good job!")
   else:
      print ("Keep practising.")
def view_history():
   try :
      with open ("scores.txt","r") as file:
         lines = file.readlines()
   except FileNotFoundError:
      print ("No score yet.")
      return
   if len(lines) ==0:
      print ("No scores yet.")
      return
   best_name = ""
   best_score = -1
   best_total = 0
   print ("Score History:")
   for number, line in enumerate(lines, start=1):
      name, score, total = line.strip().split(",")
      score = int(score)
      total = int(total)
      print (f"{number}. {name	} - {score}/{total}")
      if score > best_score:
         best_name = name
         best_score = score
         best_total = total
   print (f"Best score: {best_name} ({best_score}/{best_total})")
while True:
   print ("1. Play Quiz")
   print ("2. View Score History")
   print ("3. Exit")
   try:
      opt = int (input("Choose: "))
   except ValueError:
      print ()
      print ("Please enter a number.")
      print ()
      continue
   if opt ==1:
      print ()
      play_quiz()
      print ()
   elif opt == 2:
      print ()
      view_history()
      print ()
   elif opt == 3:
      print ()
      print ("Bye")
      print ()
      break
   else:
      print ()
      print ("Invalid operation")
      print ()
      continue
