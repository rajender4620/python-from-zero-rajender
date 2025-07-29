
from tasks.task import add_task, list_tasks, mark_as_complete, delete_task
while True:

    print("🎮 Smart Life Manager \n")

    print("1. Manage Tasks")
    print("2. Manage Expenses")
    print("3. Manage Contacts")
    print("4. Manage Notes")
    print("5. Exit")

    task = int(input("Choose the options from above :\n"))

    if task == 1:
        print("1. Manage Tasks \n")
        while True:

            print("1. Add Tasks")
            print("2. List Tasks")
            print("3. Delete Task")
            print("4. Mark as complete")
            print("5. Exit")

            mtask = int(input("Choose the option from above : \n"))

            if mtask == 1:
                tas = input("please add the task : \n")
                add_task(tas)
            elif mtask == 2:
                list_tasks()
            elif mtask == 3:
                delete_task()
            elif mtask == 4:
                print("Mark as complete Task - call function here")
                mark_as_complete()
            elif mtask == 5:
                print("Successfully existed")
                break
            else:
                print("Invalid option.")

    elif task == 2:
        print()
    elif task == 3:
        print()
    elif task == 4:
        print()
    elif task == 5:
        print("Successfully existed")
        break
    else:
        print("Invalid option.")
