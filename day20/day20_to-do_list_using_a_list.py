task = []
while True:
   print ("1. Add Task")
   print ("2. Remove Task")
   print ("3. View Task")
   print ("4. Done Tasks")
   print ("5. Exit")
   opt = int ( input ("Choose:") )
   if opt == 1:
      print ()
      task.append( input ("Enter task:"))
      print ("Task Added!")
      print ()
   elif opt ==2:
      print ()
      task_remove = input ("Enter task to remove: ")
      if task_remove in task:
        task.remove (task_remove)
        print ("Task removed!")
      else:
        print ("Task not found!")
      print ()
   elif opt == 3:
      print ()
      print ("Your tasks")
      for index, task in enumerate (task,start=1):
          print (index, task)
      print ()
   elif opt ==4:
      print ()
      for index, t in enumerate (task,start=1):
         print (index, t)
      done_task =int ( input ("Enter your done task number: "))
      if 1 <= done_task <= len(task) :
         task[done_task - 1] = task[done_task -1]+"✅" 
         print ("Done task added!")
      else:
         print ("Invalid task number")
      print ()
   elif opt ==5:
      print ()
      print ("Bye")
      print ()
      break
   else:
      print ()
      print ("Invalid option")
      print ()
      break

