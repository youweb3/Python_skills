#==============
#To-Do List App
#==============

# Liat to store tasks
tasks = []

# Function to show menu
def show_menu():
    print("====To-Do List Menu ====")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Search a task")
    print("5. Exit")
    print("=" *20)

#Main loop
while True:
    show_menu()
    choice= input("Enter your choice (1-5):")

    # Option 1: Add a task
    if choice == "1":
        task_name = input("Enter your task you want to add:")
        tasks.append(task_name)
        print(f"'{task_name}' has been added to your list.")

    # Option 2: Remove a task
    elif choice == "2":
        if not tasks:
            print("Your task list is empty. Nothing to remove.")
        else:
            print("Task:")
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}.{task}")
            try:
                task_number = int(input("Enter the number of the task to remove:"))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"'{removed_task}'has been removed from your list.")
                else:
                 print("Invalid number. Please try again.")
            except ValueError:
                print("Invalid input. please enter a number.")

    # Option 3: View tasks (Placeholder for now)   
    elif choice == "3":
        if not tasks:
            print("Your tasks list is empty.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    
    # Option 4: Search tasks        
    elif choice == "4":
        if not tasks:
            print("Your task list is empty. Nothing to search.")
        else:
            search_term = input("Enter the task name to search for:")
            found = False
            for task in tasks:
                if search_term.lower() in task.lower():
                    print(f"Found: {task}")
                    found = True
            if not found:
                print("Task not found.")
    
    
    # Option 5: Exit
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")