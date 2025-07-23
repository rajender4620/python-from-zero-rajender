user = {
    "name": "raj",
    "age": 28,
    "email": "raj@example.com",
    "skills": ["python"]
}

while True:
    print("\n🎮 MENU")
    print("1. Show Profile")
    print("2. Edit Profile")
    print("3. Add Skill")
    print("4. Remove Skill")
    print("5. Exit")

    task = int(input("Choose the task: "))

    if task == 1:
        print("\n🧾 Profile")
        for key, val in user.items():
            if isinstance(val, list):
                print(f"{key.capitalize()}:")
                for item in val:
                    print(f" - {item}")
            else:
                print(f"{key.capitalize()}: {val}")

    elif task == 2:
        field = input('which one you want to edit (name/age/email) :')
        if field in user and not isinstance(user[field], list):
            new_val = input(f'enter the new value for {field}')
            if field == 'age':
                user[field] = int(new_val)
            if field == 'name':
                user[field] = new_val
            if field == 'email':
                user[field] = new_val
        else:
            print("❌ Invalid field.")
    elif task == 3:
        new_skill = input("Enter skill to add: ")
        user["skills"].append(new_skill)
        print("✅ Skill added.")

    elif task == 4:
        remove_skill = input("Enter skill to remove: ")
        if remove_skill in user["skills"]:
            user["skills"].remove(remove_skill)
            print("🗑️ Skill removed.")
        else:
            print("❌ Skill not found.")

    elif task == 5:
        print("👋 Successfully exited.")
        break

    else:
        print("❌ Invalid choice.")
