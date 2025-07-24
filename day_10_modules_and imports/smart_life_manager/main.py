from goals_module import add_goal, view_goals
from habits_module import add_habit
from quotes_module import show_quote
from skills_module import add_skill, view_skills

while True:

    print("\n==== SMART LIFE MANAGER ====")
    print("1. Add Goal")
    print("2. View Goals")
    print("3. Add Skill")
    print("4. View Skills")
    print("5. Add Habit")
    print("6. Show Daily Quote")
    print("7. Exit")

    try:
        task = int(input("Choose an option: "))
    except ValueError:
        print("Enter a number.")
        continue

    if task == 1:
        goal = input("Enter the goal: ")
        add_goal(goal)
    elif task == 2:
        view_goals()
    elif task == 3:
        skill = input("Enter a new skill: ")
        add_skill(skill)
    elif task == 4:
        view_skills()
    elif task == 5:
        habit = input("Enter a new habit: ")
        add_habit(habit)
    elif task == 6:
        show_quote()
    elif task == 7:
        print("✅ Exiting Smart Life Manager.")
        break
    else:
        print("Choose a valid option (1–7).")
