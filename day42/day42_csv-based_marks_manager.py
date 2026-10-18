import csv
import os

FILE_NAME = "marks.csv"

def load_students():
   students = []
   try:
      with open(FILE_NAME, "r", newline="") as file:
         for row in csv.DictReader(file):
            students.append((row["roll"], row["name"], float(row["marks"])))
   except FileNotFoundError:
      pass
   return students

while True:
   print("1. Add Student")
   print("2. View All Students")
   print("3. Search by Name")
   print("4. Class Average and Topper")
   print("5. Export Toppers Report")
   print("6. Exit")
   try:
      opt = int(input("Choose: "))
   except ValueError:
      print()
      print("Please enter a number.")
      print()
      continue

   if opt == 1:
      print()
      roll = input("Enter roll number: ").strip()
      name = input("Enter name: ").strip()
      try:
         marks = float(input("Enter marks (0-100): "))
      except ValueError:
         print()
         print("Marks must be a number.")
         print()
         continue

      students = load_students()
      exists = False
      for r, n, m in students:
         if r == roll:
            exists = True

      if roll == "" or name == "":
         print("Roll number and name cannot be empty.")
      elif exists:
         print(f"Roll number {roll} already exists!")
      elif marks < 0 or marks > 100:
         print("Marks must be between 0 and 100.")
      else:
         file_is_new = not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0
         with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            if file_is_new:
               writer.writerow(["roll", "name", "marks"])
            writer.writerow([roll, name, marks])
         print("Student saved!")
      print()

   elif opt == 2:
      print()
      students = load_students()
      if len(students) == 0:
         print("No students yet.")
      else:
         print("Roll | Name | Marks")
         for roll, name, marks in students:
            print(f"{roll} | {name} | {marks}")
      print()

   elif opt == 3:
      print()
      search_text = input("Enter name to search: ").lower().strip()
      students = load_students()
      found = False
      for roll, name, marks in students:
         if search_text in name.lower():
            print(f"{roll} | {name} | {marks}")
            found = True
      if not found:
         print("No matching students found.")
      print()

   elif opt == 4:
      print()
      students = load_students()
      if len(students) == 0:
         print("No students yet.")
      else:
         total = 0
         top_name = students[0][1]
         top_marks = students[0][2]
         for roll, name, marks in students:
            total += marks
            if marks > top_marks:
               top_marks = marks
               top_name = name
         average = total / len(students)
         print(f"Class average: {round(average, 2)}")
         print(f"Topper: {top_name} ({top_marks})")
      print()

   elif opt == 5:
      print()
      students = load_students()
      if len(students) == 0:
         print("No students yet.")
      else:
         count = 0
         with open("toppers.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["roll", "name", "marks"])
            for roll, name, marks in students:
               if marks >= 75:
                  writer.writerow([roll, name, marks])
                  count += 1
         if count == 0:
            print("No student scored 75 or above.")
         else:
            print(f"Report saved to toppers.csv ({count} students)")
      print()

   elif opt == 6:
      print()
      print("Bye")
      print()
      break

   else:
      print()
      print("Invalid option")
      print()
