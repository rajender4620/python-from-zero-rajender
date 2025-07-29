
from pathlib import Path


TASKS_FILE = Path("smart-life-manager/tasks/tasks.txt")


def add_task(task):
    with TASKS_FILE.open('a') as f:
        f.write(f"[] {task}\n")
        print("Successfully added task")


def list_tasks():
    if TASKS_FILE.exists():
        with TASKS_FILE.open("r") as f:
            tasks = f.readlines()
            print("Tasks : \n")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task.strip()}")
    else:
        print("No tasks found.")


# def delete_task(tasknum):
#     if TASKS_FILE.exists():
#         with TASKS_FILE.open("r") as f:
#             tasks = f.readlines()

#         if 1 <= tasknum <= len(tasks):
#             removed = tasks.pop(tasknum - 1)

#             with TASKS_FILE.open("w") as f:
#                 f.writelines(tasks)

#             print(f"✅ Deleted: {removed.strip()}")
#         else:
#             print("❌ Invalid task number.")
#     else:
#         print("No tasks found.")

def delete_task():
    if not TASKS_FILE.exists():
        print("No tasks found.")
        return

    with TASKS_FILE.open("r") as f:
        all_tasks = f.readlines()

    # Filter only incomplete tasks
    incomplete_tasks = [(i, task) for i, task in enumerate(
        all_tasks) if task.startswith("[]")]

    if not incomplete_tasks:
        print("✅ No incomplete tasks to delete.")
        return

    print("Which task do you want to delete?")
    for menu_index, (real_index, task) in enumerate(incomplete_tasks, start=1):
        print(f"{menu_index}. {task.strip()}")

    try:
        choice = int(input("Enter the number to delete: "))
        if 1 <= choice <= len(incomplete_tasks):
            target_index = incomplete_tasks[choice - 1][0]
            removed = all_tasks.pop(target_index)

            with TASKS_FILE.open("w") as f:
                f.writelines(all_tasks)

            print(f"🗑️ Deleted: {removed.strip()}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


# def mark_as_complete():
#     if TASKS_FILE.exists():
#         with TASKS_FILE.open("r") as f:
#             tasks = f.readlines()

#         print("which task you want to mark as complete")
#         for i, t in enumerate(tasks, start=1):
#             print(f"{i}. {t.strip()}")

#     choice = int(input("Please enter the number to mark as complete : \n"))
#     if 1 <= choice <= len(tasks):
#         tasks[choice - 1] = tasks[choice - 1].replace("[]", "[x]")

#         with TASKS_FILE.open("w") as f:
#             f.writelines(tasks)

#         print("✅ Task marked as complete.")


def mark_as_complete():
    if not TASKS_FILE.exists():
        print("No tasks found.")
        return

    with TASKS_FILE.open("r") as f:
        all_tasks = f.readlines()

    # Filter only incomplete tasks
    incomplete_tasks = [(i, task) for i, task in enumerate(
        all_tasks) if task.startswith("[]")]

    if not incomplete_tasks:
        print("🎉 All tasks are already complete!")
        return

    print("Which task do you want to mark as complete?")
    for menu_index, (real_index, task) in enumerate(incomplete_tasks, start=1):
        print(f"{menu_index}. {task.strip()}")

    try:
        choice = int(input("Enter the number to mark as complete: "))
        if 1 <= choice <= len(incomplete_tasks):
            # Real index in all_tasks
            target_index = incomplete_tasks[choice - 1][0]
            all_tasks[target_index] = all_tasks[target_index].replace(
                "[]", "[x]")

            with TASKS_FILE.open("w") as f:
                f.writelines(all_tasks)

            print("✅ Task marked as complete.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")
