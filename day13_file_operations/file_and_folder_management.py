
import os
import shutil
import pathlib

# below operations will happen under the current working directory

# Current working directory
print("📍 Current Directory:", os.getcwd())

# List contents
print("📦 Files and Folders:", os.listdir())

# # Create new folder
# os.mkdir("demo_folder")

# # Rename folder
# os.rename("demo_folder", "renamed_folder")


# Remove folder (only if empty)
os.rmdir("renamed_folder")
