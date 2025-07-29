import os
import shutil

# Create a sample file
with open("demo.txt", "w") as f:
    f.write("This file is for shutil demo.")

# # Copy the file
# shutil.copy("demo.txt", "demo_copy.txt")
# print("✅ File copied")

# # Move the file
# shutil.move("demo_copy.txt", "moved_demo.txt")
# print("📦 File moved")


# # Make a new folder
# os.mkdir("test_folder")

# # Move file into folder
# shutil.move("moved_demo.txt", "test_folder/moved_demo.txt")
# print("📂 File moved into folder")

# Delete folder and its contents
shutil.rmtree("test_folder")
print("🧹 Folder and contents deleted")

# Clean up original
os.remove("demo.txt")
