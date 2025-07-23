# 📦 Python Learning Progress – Rajender

## ✅ Day 01 — Basics

### ✅ Variables & Types

- Learned to declare variables dynamically (no type keywords like Dart)
- `name = "demon slayer"`
- Used `type()` to check variable types

### ✅ Printing

- Used `print(name)`
- Printed multiple items: `print(type(releasedData), name)`

---

### ✅ Functions

- Defined a function with `def`
  Example:

  ```python
  def reverse_string(s):
      ...
  ```

## ✅ Day 02 — Collections & Functions

### ✅ Lists

- Created list: `numbers = [10, 20, 30]`
- Appended items with `numbers.append(40)`
- Loop over items: `for n in numbers`
- Loop by index: `for i in range(len(numbers))`
- Wrote manual `sum_list` and `find_max` functions

---

### ✅ Tuples

- Immutable ordered collections
- Cannot change, append, or remove after creation

---

### ✅ Sets

- Unique, unordered collections
- Used `add()` to insert
- Used `not in` to manually avoid duplicates
- Understood: set automatically keeps only unique items

---

### ✅ Dictionaries

- Key–value pairs: `{'name': 'Rajender', 'age': 26}`
- Access: `person['name']`
- Safe access: `person.get('name')`
- Add new key: `person['email'] = ...`
- Loop with:

  ```python
  for key, val in person.items():
      print(key, val)
  ```

---

## ✅ Day 08 — Profile Manager Project

### ✅ Built interactive menu-driven app

- Menu using `while True` loop
- CRUD operations on dictionary values
- Handled `list` fields like `skills`
- Used `isinstance(val, list)` to check type
- Handled editing non-list fields like name, age, email
- Used `.append()` and `.remove()` for skill updates
- Gracefully handled invalid inputs and exits

### ✅ Sample logic:

```python
if isinstance(val, list):
    for item in val:
        print("-", item)
```

### ✅ Learned:

- Type checking
- Dictionary updates
- Nested conditionals in menu logic
- Input validation basics
