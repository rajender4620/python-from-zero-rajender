from pathlib import Path

# Define the markdown content

md_content = """# 📦 Python Learning Progress – Rajender

## ✅ Day 01 — Basics

### ✅ Variables & Types

- Declared variables dynamically (no type keywords like Dart)
- Used `type()` to check variable types

### ✅ Printing

- Used `print(name)` and printed multiple items
- Example: `print(type(releasedData), name)`

---

## ✅ Day 02 — Collections & Functions

### ✅ Lists

- Created list: `numbers = [10, 20, 30]`
- Used `.append()` to add items
- Loop over values and indices using `for` and `range(len(...))`
- Wrote custom functions like `sum_list`, `find_max`

### ✅ Tuples

- Immutable ordered collections
- Can't add/remove after creation

### ✅ Sets

- Unique, unordered items
- Used `.add()` and `not in` to avoid duplicates
- Set removes duplicates automatically

### ✅ Dictionaries

- Key-value pairs
- Accessed with `[]` and `.get()`
- Modified by assigning new keys/values
- Looped with `.items()`

---

## ✅ Day 08 — Profile Manager Project

### ✅ Built an interactive menu app

- Used `while True` for menu
- CRUD on dictionary fields
- Handled `list` fields like `skills`
- Checked type using `isinstance(val, list)`
- Appended/removed from list
- Validated input

### ✅ Concepts reinforced:

- Type checks
- Conditional logic inside loops
- Error handling and user interaction

---

## ✅ Day 09 — Files: Read & Write

### ✅ `with open(...)` for file handling

- Wrote to files: `'w'`, `'a'`
- Read with `'r'`
- Stripped newlines using `.strip()`
- Handled line-by-line reading

### ✅ Mini-Project: Smart Life Manager

- Managed goals, skills, habits
- Stored data in separate `.txt` files

---

## ✅ Day 10 — Modules & Imports

### ✅ Modularization

- Split project into:
  - `main.py`, `goals_module.py`, `skills_module.py`, etc.
- Imported functions using:
  ```python
  from goals_module import add_goal
  ```
