def add_skill(skill):
    if not skill:
        print("Enter a valid skill.")
    else:
        with open("skills.txt", "a") as f:
            f.write(skill + "\n")
        print("✅ Skill added.")

def view_skills():
    try:
        with open("skills.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No skills added yet.")
                return
            print("Skills:")
            for line in lines:
                print(f"- {line.strip()}")
    except FileNotFoundError:
        print("Skills file not found.")
