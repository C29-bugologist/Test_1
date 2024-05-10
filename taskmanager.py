my_Tasks = []
completed_task = []
#task_function = int(input("Enter 1 for adding a new task\nEnter 2 for removing a completed task\nEnter 3 for viewing all tasks\n"))
def add_task():
    task_add = input("What is the task that you want to add?\n")
    my_Tasks.append(task_add)
def view_task():
    print(my_Tasks)
    print(completed_task)
def remove_completed():
    task_remove = input("What is the task that you want to remove?\n")
    if task_remove in my_Tasks:
         my_Tasks.remove(task_remove)
         completed_task.append(task_remove)
    else:
             print("No such Task found")

while True:
    print("----------Task_Manager----------\n")
    task_function = int(input("Enter 1 for adding a new task\nEnter 2 for removing a completed task\nEnter 3 for viewing all tasks\nEnter 4 for Ending the program resting the list"))

    if task_function == 3:
        view_task()
    elif task_function == 1:
        add_task()
    elif task_function == 2:
         remove_completed()
      
    elif task_function == 4:
        break   
    else:
        print("Choose either 1, 2, or 3")
print("goodby")