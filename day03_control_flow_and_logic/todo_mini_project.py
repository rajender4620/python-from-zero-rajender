"""
🎯 Mini Project: To-Do List App (Console)
Features:

Show menu:

markdown
Copy
Edit
1. Add task
2. View tasks
3. Delete task
4. Exit
User picks option using input()

Store tasks in a list

Loop until user exits


"""


tasks = []
while True:
    print("\nMENU")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    task = int(input("Enter your choice (1-4): "))

    if task == 1:
        enteredtask = input("Enter the task: ")
        tasks.append(enteredtask)
        print("✅ Task added.")

    elif task == 2:
        if not tasks:
            print("🚫 No tasks.")
        else:
            print("📋 Your tasks:")
            for t in tasks:
                print("- " + t)
    elif task == 4:
        print("👋 Exiting...")
        break
    elif task == 3:
        tasks.clear()
        print("successfully deleted tasks")

    else:
        print("❌ Invalid option.")
