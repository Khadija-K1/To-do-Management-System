# ------ Python Mini Project # 01

# ------- To do mangement system:
# User can: Add, View, Update, and delete tasks. 
# User cana also mark tasks as done.
# File handling for data persistence.


# List to store tasks
tasks = []

# Create a file to store tasks: 
with open ("tasks.txt", "a") as f: 
     pass

# Loading tasks from file into the list.
with open ("tasks.txt", "r") as f: 
     while True: 
          data = f.readline().strip()
          if data == "":
               break
          tasks.append(data)

# Changes being stored in the file alongside
def change_tasks(tasks):
     with open ("tasks.txt", "w") as f: 
          for t in tasks: 
                f.write(f"{t}\n")

# Display Tasks Function:
def display_tasks(tasks): 
       if len(tasks) == 0:
              print("No tasks yet")
       else: 
              print("\nYour Tasks")
              for i, t in enumerate(tasks, start=1):
                  print(f"{i}. {t}")


# Main Menu:
while True:
    print("\n=====To-Do MENU=====")
    print("\n1- Add tasks")
    print("2- View tasks")
    print("3- Update tasks")
    print("4- Delete task")
    print("5- Mark tasks")
    print("6- Exit")

    menu_choice = input("Enter your choice: ")

    if menu_choice == "1": 

        while True: 
           task = input("Add tasks: ").lower()
           tasks.append(task)
           change_tasks(tasks)

           while True:
               task_choice = input("Do u want to add more tasks (yes/no): ").lower()

               if task_choice == "yes" or task_choice == "no": 
                   break
               else:
                   print("Invalid choice! Enter yes/no")

           if task_choice == "no":
                break

    elif menu_choice == "2":
         if len(tasks) == 0:
              print("No tasks yet")
              continue
         display_tasks(tasks)

    elif menu_choice == "3":
              if len(tasks) == 0:
                   print("No tasks yet")
                   continue
              display_tasks(tasks)

              try:
                  update_choice = int(input("Which task do u want to update: "))

                  if update_choice < 1 or update_choice > len(tasks):
                      print("Invalid number")
                  else: 
                       updated_choice = input("Enter the updated one: ")
                       num = update_choice - 1
                       tasks[num] = updated_choice
                       change_tasks(tasks)
                       print(f"Task updated to: {updated_choice}")
              except ValueError: 
                        print("Invalid, Try again...")


    elif menu_choice == "4": 
             if len(tasks) == 0:
                  print("No tasks yet")
                  continue
             display_tasks(tasks)

             try:
                  delete_choice = int(input("What task you want to delete, enter number: "))

                  if delete_choice < 1 or delete_choice > len(tasks):
                      print("Invalid number")
                  else: 
                       final = delete_choice - 1 
                       del_task = tasks[final]
                       del tasks[final]
                       change_tasks(tasks)
                       print(f"Task Deleted: {del_task}")
             except ValueError:
                   print("Invalid, Please enter a number")


    elif menu_choice == "5": 
               if len(tasks) == 0:
                    print("No tasks yet")
                    continue
               display_tasks(tasks)

               try: 
                    mark_choice = int(input("Which task do u want to mark: "))
                    if mark_choice < 1 or mark_choice > len(tasks):
                       print("Invalid number")
                    else:
                          num = mark_choice - 1 
                          if "(Done)" in tasks[num]:
                             print("Task is already marked as completed")
                          else: 
                              tasks[num]+= " " + "(Done)"
                              change_tasks(tasks)
                              # tasks[num] = tasks[num]+ " " + "(Done)"
                              print("Task is marked as done")
               except ValueError:
                   print("Invalid input! Enter a number")


    elif menu_choice == "6": 
         print("Exiting...")
         break
    
    else: 
          print("Invalid choice")

print("Program ended")