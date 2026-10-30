# Working on task priority feature

tasks = []


def show_tasks():
    if not tasks:
        print("No tasks found.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{number}. {task['title']} - {status}")


def add_task():
    title = input("Enter task name: ").strip()

    if title:
        tasks.append({"title": title, "completed": False})
        print("Task added successfully.")
    else:
        print("Task name cannot be empty.")


def complete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def show_task_count():
    print(f"Total tasks: {len(tasks)}")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n--- Python Task Manager ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Exit")
    print("5. Delete task")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    elif choice == "5":
        delete_task()
    else:
        print("Invalid choice. Try again.")
