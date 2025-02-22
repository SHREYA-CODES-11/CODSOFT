# To-do tasks list mini project
import json
import os

# File to store tasks
TODO_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from a JSON file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    """Add a new task."""
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            status = "✔ Completed" if task["completed"] else "❌ Pending"
            print(f"{idx}. {task['task']} - {status}")

def mark_completed(tasks, task_number):
    """Mark a task as completed."""
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_number - 1]['task']}' marked as completed!")
    else:
        print("Invalid task number.")

def remove_task(tasks, task_number):
    """Remove a task."""
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['task']}' removed successfully!")
    else:
        print("Invalid task number.")

def main():
    """Main function to handle the to-do list menu."""
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter task: ").strip()
            if task:
                add_task(tasks, task)
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            view_tasks(tasks)
            try:
                task_number = int(input("Enter task number to mark as completed: "))
                mark_completed(tasks, task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            view_tasks(tasks)
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(tasks, task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Exiting To-Do List Application. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()