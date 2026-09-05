while True:
   try:
      print ()
      print ("BMI CALCULATER")
      print ("-----------------------------------------------------")
      kg0 = input("Enter your weight(kg) or press q (to Quit):")
 
      if kg0 == "q":
         print ()
         print ("==========================================")
         print ()
         print ("bye")
         print ()
         print ("==========================================")
         print ()
         print ("-----------------------------------------------------")
         break

      height = float(input("Enter your height(m):"))

      kg = float (kg0)

      bmi = kg / (height * height)

      print ()
      print ("=============================================")
      print ()
      print ("Your BMI is ",round(bmi,2))

      if bmi < 18.5:
         cgy = "Underweight"
      elif 18.5 <= bmi < 25:
         cgy = "Normal weight"
      elif 25 <= bmi < 30:
         cgy = "Overweight"
      elif 30 <= bmi:
         cgy = "Obese"

      print ("Category:",cgy)

      print ()
      print ("=============================================")
      print ()
      print ("-----------------------------------------------------")

   except ZeroDivisionError:

      print ()
      print ("=============================================")
      print ()
      print ("Invaid  height of 0 Enter correct height")
      print ()
      print ("=============================================")
      print ("-----------------------------------------------------")
