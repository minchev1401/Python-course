tasks = ["start the engine",
         "stop the engine",
         "chek for errors",
         "chek the oil level"]

def view_tasks():
        if not tasks:
            print("There is haven't any tasks yet")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            
def menu():
    
      print("""
1. View tasks.
2. Add new task.
3. Edit task.
4. Change tasks position.
5. Delete task.
6. Menu
7. Exit

To select an action, enter the appropriate number!\n""")
      
      
print("\nTasks manager.")

while True:
    try:
        menu()
        choice = str(input("Choose action: "))
    
        if choice == "1":
            view_tasks()
            
        elif choice == "2":
            new_task = (input("Enter the new task: ")).lower()
            tasks.append(new_task)
            print(f"The task '{new_task}' was added to tasks!")
            view_tasks()
            
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Choose the index of task you wont to edit: ")) -1
                edited_task = str(input("Enter the new name: ")).lower()
                tasks[index] = edited_task
                print(f"The task with index {index + 1} was changed to '{edited_task}'.")
                view_tasks()
            except (ValueError, IndexError):
                print("Invalid task index! Try again!")
                
        elif choice == "4":
            view_tasks()
            try:
                index_1 = int(input("Choose first task index: ")) -1
                index_2 = int(input("Choose second task index: ")) -1
                tasks[index_1], tasks[index_2] = tasks[index_2], tasks[index_1]
                print(f"Tasks with positions '{index_1}' and '{index_2}' was swaped!")
                view_tasks()
            except (ValueError, IndexError):
                print("Invalid task index! Try again!")
                
        elif choice == "5":
            view_tasks()
            delete_choice = str(input("Choose how to delete task:\n'i' - delete by index\n't' - delete by Title\n>: ")).lower()
            try:
                if delete_choice == "i":
                    delete_index = int(input("Enter the index of the task you wont to delete: ")) -1
                    deleted_task = tasks.pop(delete_index)
                    print(f"Task with index '{delete_index} was deleted!")
                    view_tasks()
                elif delete_choice == "t":
                    delete_title = str(input("Enter the title of the task you wont to delete: ")).lower()
                    if delete_title in tasks:
                        tasks.remove(delete_title)
                        print(f"Task '{delete_title}' was deleted!")
                        view_tasks()
                    else:
                        print(f"The'{delete_title}' is not in Tasks!")
            except (ValueError, IndexError):
                print("Invalid index or title. Try again!")
        elif choice == "6":
            menu()
                
        elif choice == "7":
            break
        
        else:
            print("Invalid choice. Please try again!")
            
    except (ValueError):
        print("Invalid choice. Please try again!")
        
        
        
            
            
            
        
        
        
        


