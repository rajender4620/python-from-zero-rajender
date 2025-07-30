
from tasks.task import add_task, list_tasks, mark_as_complete, delete_task
from contacts.contacts import add_contacts, list_contacts, delete_contact
from expenses.expenses import add_expenses, total_spends, expenses_details, total_spending_by_category
import notes.notes
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
        print("2. Manage Expenses \n")

        while True:

            print("1. Add Expense (amount, category, date)")
            print("2. Show Total Spent")
            print("3. Show Spending Per Category")
            print("4. Total Details")
            print("5. Exit")

            eTask = int(input("Choose the option from above : \n"))

            if eTask == 1:
                add_expenses()
            elif eTask == 2:
                total_spends()
            elif eTask == 3:
                total_spending_by_category()
            elif eTask == 4:
                expenses_details()
            elif eTask == 5:
                print("Successfully existed")
                break
            else:
                print("Invalid option.")

    elif task == 3:
        print("Manage Contacts \n")
        while True:

            print("1. Add Contact — name, phone, email")
            print("2. List Contacts — display all")
            print("3. Search Contact — by name or phone")
            print("4. Delete Contact")
            print("5. Update Contact")
            print("6. Exit")

            ctask = int(input("Choose the option from above : \n"))

            if ctask == 1:
                add_contacts()
            elif ctask == 2:
                list_contacts()
            elif ctask == 3:
                print
            elif ctask == 4:
                delete_contact()
            elif ctask == 5:
                print
            elif ctask == 6:
                print("Successfully existed")
                break
            else:
                print("Invalid option.")

    elif task == 4:
        print("4. Manage Notes\n")
        while True:
            print("1. Add Note")
            print("2. List Notes")
            print("3. View Note")
            print("4. Delete Note")
            print("5. Update Note")
            print("6. Exit")

            ntask = int(input("Choose the option from above : \n"))

            if ntask == 1:
                notes.notes.add_note()
            elif ntask == 2:
                notes.notes.list_notes()
            elif ntask == 3:
                notes.notes.view_note()
            elif ntask == 4:
                notes.notes.delete_note()
            elif ntask == 5:
                notes.notes.update_note()
            elif ntask == 6:
                print("Successfully exited")
            break

    elif task == 5:
        print("Successfully existed")
        break
    else:
        print("Invalid option.")
