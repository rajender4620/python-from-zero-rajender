import random

quotes = [
    "Discipline is the bridge between goals and accomplishment.",
    "What you do today can improve all your tomorrows.",
    "Success doesn’t come from what you do occasionally, it comes from what you do consistently.",
    "Small habits lead to big changes.",
    "You don’t need more motivation, you need more discipline."
]

GOALS_FILE = "C:/python-from-zero-rajender/day09_read_and_write_flies/smart_life_manager/goals.txt"
SKILLS_FILE = "C:/python-from-zero-rajender/day09_read_and_write_flies/smart_life_manager/skills.txt"
HABITS_FILE = "C:/python-from-zero-rajender/day09_read_and_write_flies/smart_life_manager/habits.txt"


def view_goals():
    with open(GOALS_FILE, "r") as f:
        content = f.readlines()
        print("📌 Goals:")
        for goal in content:
            print(f"- {goal.strip()}")


def add_goal(goal):
    if not goal.strip():
        print("⚠️ Enter a valid goal.")
    else:
        with open(GOALS_FILE, 'a') as f:
            f.write(goal.strip() + "\n")
        print("✅ Goal added.")


def add_skill(skill):
    if not skill.strip():
        print("⚠️ Enter a valid skill.")
    else:
        with open(SKILLS_FILE, 'a') as f:
            f.write(skill.strip() + "\n")
        print("✅ Skill added.")


def view_skills():
    with open(SKILLS_FILE, 'r') as f:
        lines = f.readlines()
        if not lines:
            print("No skills added yet.")
        else:
            print("🧠 Skills:")
            for skill in lines:
                print(f"- {skill.strip()}")


def add_habit(habit):
    if not habit.strip():
        print("⚠️ Enter a valid habit.")
    else:
        with open(HABITS_FILE, 'a') as f:
            f.write(habit.strip() + "\n")
        print("✅ Habit added.")


def view_habits():
    with open(HABITS_FILE, 'r') as f:
        lines = f.readlines()
        if not lines:
            print("No habits added yet.")
        else:
            print("🔥 Habits:")
            for habit in lines:
                print(f"- {habit.strip()}")


while True:
    print("\n===== SMART LIFE MANAGER =====")
    print("1. Add Goal")
    print("2. View Goals")
    print("3. Add Skill")
    print("4. View Skills")
    print("5. Add Habit")
    print("6. View Habits")
    print("7. Show Daily Quote")
    print("8. Exit")

    try:
        task = int(input("Choose an option: "))
    except ValueError:
        print("⚠️ Invalid input. Enter a number.")
        continue

    if task == 1:
        add_goal(input("Enter a goal: "))
    elif task == 2:
        view_goals()
    elif task == 3:
        add_skill(input("Enter a new skill: "))
    elif task == 4:
        view_skills()
    elif task == 5:
        add_habit(input("Enter a new habit: "))
    elif task == 6:
        view_habits()
    elif task == 7:
        print("\n💡 Daily Quote:")
        print(random.choice(quotes))
    elif task == 8:
        print("👋 Exiting. Stay disciplined!")
        break
    else:
        print("⚠️ Choose a valid option (1-8).")
