import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the tasks.json file. If the file doesn't exist or is invalid, return an empty list."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: tasks.json is corrupted or contains invalid JSON. Returning an empty task list.")
            return []
    return []

def save_tasks(tasks):
    """Save tasks to the tasks.json file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """Add a new task with the given description."""
    tasks = load_tasks()
    tasks.append({"description": description, "status": "incomplete"})
    save_tasks(tasks)
    print("Task added successfully!")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        return "No tasks available."

    task_list = "Your Tasks:\n"
    for index, task in enumerate(tasks, 1):
        task_list += f"{index}. [{'✓' if task['status'] == 'complete' else '✗'}] {task['description']}\n"
    return task_list

def complete_task(task_number):
    """Mark the given task as complete."""
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["status"] = "complete"
        save_tasks(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    """Delete the given task from the list."""
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted task: {deleted_task['description']}")
    else:
        print("Invalid task number.")

def main():
    """Main function to run the task management application."""
    while True:
        print("\nTask Management App")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            try:
                task_number = int(input("Enter task number to mark as complete: "))
                complete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            try:
                task_number = int(input("Enter task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
