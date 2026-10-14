def load_students():
   students = []
   try:
      with open("students.txt", "r") as file:
         for line in file:
            roll, name, marks = line.strip().split(",")
            students.append((roll, name, float(marks)))
   except FileNotFoundError:
      pass
   return students

def save_students(students):
   with open("students.txt", "w") as file:
      for roll, name, marks in students:
         file.write(f"{roll},{name},{marks}\n")

while True:
   print("1. Add Student")
   print("2. View All Students")
   print("3. Search by Roll Number")
   print("4. Class Average and Topper")
   print("5. Delete Student")
   print("6. Update Marks")
   print("7. Exit")
   opt = int(input("Choose: "))

   if opt == 1:
      print()
      roll = input("Enter roll number: ").strip()
      name = input("Enter name: ").replace(",", " ")
      marks = float(input("Enter marks (0-100): "))

      students = load_students()
      exists = False
      for r, n, m in students:
         if r == roll:
            exists = True

      if roll == "" or name.strip() == "":
         print("Roll number and name cannot be empty.")
      elif exists:
         print(f"Roll number {roll} already exists!")
      elif marks < 0 or marks > 100:
         print("Marks must be between 0 and 100.")
      else:
         with open("students.txt", "a") as file:
            file.write(f"{roll},{name},{marks}\n")
         print("Student saved!")
      print()

   elif opt == 2:
      print()
      students = load_students()
      if len(students) == 0:
         print("No students yet.")
      else:
         for roll, name, marks in students:
            print(f"{roll} | {name} | {marks}")
      print()

   elif opt == 3:
      print()
      search_roll = input("Enter roll number: ").strip()
      students = load_students()
      found = False
      for roll, name, marks in students:
         if roll == search_roll:
            print(f"Found: {name}, marks {marks}")
            found = True
      if not found:
         print("Student not found.")
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
      del_roll = input("Enter roll number to delete: ").strip()
      students = load_students()
      new_students = []
      found = False
      deleted_name = ""
      for roll, name, marks in students:
         if roll == del_roll:
            found = True
            deleted_name = name
         else:
            new_students.append((roll, name, marks))

      if not found:
         print("Student not found.")
      else:
         confirm = input(f"Delete {deleted_name}? (y/n): ").lower()
         if confirm == "y":
            save_students(new_students)
            print(f"{deleted_name} deleted.")
         else:
            print("Delete cancelled.")
      print()

   elif opt == 6:
      print()
      up_roll = input("Enter roll number to update: ").strip()
      students = load_students()
      found = False
      for roll, name, marks in students:
         if roll == up_roll:
            found = True

      if not found:
         print("Student not found.")
      else:
         new_marks = float(input("Enter new marks (0-100): "))
         if new_marks < 0 or new_marks > 100:
            print("Marks must be between 0 and 100.")
         else:
            new_students = []
            for roll, name, marks in students:
               if roll == up_roll:
                  new_students.append((roll, name, new_marks))
               else:
                  new_students.append((roll, name, marks))
            save_students(new_students)
            print("Marks updated!")
      print()

   elif opt == 7:
      print()
      print("Bye")
      print()
      break

   else:
      print()
      print("Invalid option")
      print()
