from pathlib import Path

# # 📍 Define a path object
# my_path = Path("sample_folder")

# # ✅ Create the folder (if not exists)
# my_path.mkdir(exist_ok=True)
# print("📁 Folder created")

# # ✍️ Create a file inside it
# file = my_path / "demo.txt"
# file.write_text("Pathlib is clean!")
# print("📝 File written")

# # 📖 Read from the file
# content = file.read_text()
# print("📖 File content:", content)

# # 🗑️ Delete file
# file.unlink()
# print("🗑️ File deleted")

# # ❌ Delete folder
# my_path.rmdir()
# print("📂 Folder deleted")

# 📍 Define a path object
# my_path = Path("sample_folder")
# print(my_path)

# # my_path.mkdir(exist_ok=True)
# # print("📁 Folder created")

# # ✍️ Create a file inside it
# file = my_path / "demo.txt"
# file.write_text("Pathlib is clean!")
# print("📝 File written")

# # 📖 Read from the file
# content = file.read_text()
# print("📖 File content:", content)

# # 🗑️ Delete file
# file.unlink()
# print("🗑️ File deleted")

# # ❌ Delete folder
# my_path.rmdir()
# print("📂 Folder deleted")


# old_path = Path("Day 13 — OOP (Classes, Objects, etc.)")

# new_path = Path("Day 14 — OOP (Classes, Objects, etc.)")
# my_path.mkdir(exist_ok=True)

# old_path.rename(new_path)


# folder_path = (Path("Day 14 — OOP (Classes, Objects, etc.)") / "file.py")
# folder_path.unlink()


slm = Path("smart-life-manager")
# slm.mkdir(exist_ok=True)

# (slm / "main.py").touch() created file through pathlib

# (slm / "tasks").mkdir(exist_ok=True) created a folder

# (slm / "tasks/tasks.py").touch()  created a file inside folder in folder

# (slm / "expenses").mkdir(exist_ok=True)

# (slm / "expenses/expenses.txt").touch()


# (slm / "contacts").mkdir(exist_ok=True)

# (slm / "contacts/contacts.txt").touch()


# (slm / "notes").mkdir(exist_ok=True)
