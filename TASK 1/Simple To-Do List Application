def display_todo_list(todo_list):
    if not todo_list:
        print("The to-do list is empty.\n")
    else:
        for idx, task in enumerate(todo_list, start=1):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"{idx}. {task['task']} - {status}")
        print()

def add_task(todo_list):
    task_description = input("Enter the task description: ")
    todo_list.append({'task': task_description, 'completed': False})
    print("Task added.\n")

def mark_task_completed(todo_list):
    display_todo_list(todo_list)
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(todo_list):
        todo_list[task_number - 1]['completed'] = True
        print("Task marked as completed.\n")
    else:
        print("Invalid task number.\n")

def remove_task(todo_list):
    display_todo_list(todo_list)
    task_number = int(input("Enter the task number to remove: "))
    if 1 <= task_number <= len(todo_list):
        todo_list.pop(task_number - 1)
        print("Task removed.\n")
    else:
        print("Invalid task number.\n")

def main():
    todo_list = []
    while True:
        print("Options:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            mark_task_completed(todo_list)
        elif choice == '4':
            remove_task(todo_list)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()
