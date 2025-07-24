def view_goals():
    with open("goals.txt", "r") as f:
        content = f.readlines()
        print("Goals:")
        for goal in content:
            print(f"- {goal.strip()}")

def add_goal(goal):
    if not goal:
        print("Enter a valid goal.")
    else:
        with open("goals.txt", "a") as f:
            f.write(goal + "\n")
        print("✅ Goal added.")
