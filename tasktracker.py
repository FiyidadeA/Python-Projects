tasks = []

def add_task(title):
    task = {"title": title, "done": False}
    tasks.append(task)
    print(f"Task added: {title}")

def list_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(f"{i + 1}. {task['title']} [{status}]")

def complete_task(number):
    index = number - 1
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    tasks[index]["done"] = True
    print(f"Task marked as done: {tasks[index]['title']}")

def delete_task(number):
    index = number - 1
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    removed = tasks.pop(index)
    print(f"Task deleted: {removed['title']}")

def menu():
    while True:
        print("\n--- Task Tracker ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            number = int(input("Enter task number to mark as done: "))
            complete_task(number)
        elif choice == "4":
            list_tasks()
            number = int(input("Enter task number to delete: "))
            delete_task(number)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")

menu()
