import json
import os
FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nTO-DO LIST")
    print("-" * 40)

    for i, task in enumerate(tasks, start=1):
        status = "✓ Completed" if task["completed"] else "✗ Pending"
        print(f"{i}. {task['task']} [{status}]")

# Mark task complete
def complete_task(tasks):
    view_tasks(tasks)

    try:
        task_num = int(input("\nEnter task number to complete: "))
        tasks[task_num - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number!")

# Update task
def update_task(tasks):
    view_tasks(tasks)

    try:
        task_num = int(input("\nEnter task number to update: "))
        new_task = input("Enter new task description: ")
        tasks[task_num - 1]["task"] = new_task
        save_tasks(tasks)
        print("Task updated successfully!")
    except (ValueError, IndexError):
        print("Invalid task number!")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_num = int(input("\nEnter task number to delete: "))
        removed_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed_task['task']}")
    except (ValueError, IndexError):
        print("Invalid task number!")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n")
        print("=" * 40)
        print("      TO-DO LIST APPLICATION")
        print("=" * 40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            update_task(tasks)

        elif choice == "5":
            delete_task(tasks)

        elif choice == "6":
            print("Thank you for using To-Do List Application!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
