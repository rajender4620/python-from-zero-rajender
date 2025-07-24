def add_habit(habit):
    if not habit:
        print("Enter a valid habit.")
    else:
        with open("habits.txt", "a") as f:
            f.write(habit + "\n")
        print("✅ Habit added.")
