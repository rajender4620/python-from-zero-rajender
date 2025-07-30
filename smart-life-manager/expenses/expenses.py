from pathlib import Path
from datetime import date

EXPENSES_FILE = Path("smart-life-manager/expenses/expenses.txt")


def add_expenses():
    amount = input("Enter amount: ₹ ")
    category = input("Enter category (e.g., Food, Travel): ")
    today = date.today().isoformat()  # yyyy-mm-dd

    with EXPENSES_FILE.open("a") as f:
        f.write(f"{amount} | {category} | {today}\n")

    print("✅ Expense added.")


def total_spends():
    total = 0
    if EXPENSES_FILE.exists():
        with EXPENSES_FILE.open("r") as f:
            expenses = f.readlines()
            for i, e in enumerate(expenses):
                parts = e.strip().split("|")
                if len(parts) > 0:
                    try:
                        amount_str = parts[0].strip()
                        total += float(amount_str)
                    except ValueError:
                        print(f"Skipping invalid line: {e.strip()}")

    print(f"Total amount spent : {total}")
    return total


def expenses_details():
    if EXPENSES_FILE.exists():
        with EXPENSES_FILE.open("r") as f:
            content = f.readlines()
            print("amount , category")
            for i, c in enumerate(content):
                print(f"{i}. {c.replace(" | ", " , ")}")


# def total_spending_by_category():

#     total = 0
#     choose = input("Please enter the category")
#     formated = choose.lower().strip()
#     try:
#         if EXPENSES_FILE.exists():
#             with EXPENSES_FILE.open("r") as f:
#                 expenses = f.readlines()
#                 print(f"Total spend by category {formated}")

#                 for i, e in enumerate(expenses):
#                     replaced = e.replace(" | ", " ")
#                     parts = replaced.split()
#                     categ = parts[1].lower()
#                     if categ == formated:
#                         amount_str = parts[0].strip()
#                         total = total + float(amount_str)
#                     else:
#                         print("category not found")
#     except ValueError:
#         print("Please enter valid category ")

#     print(f"Total spend by category : {total}")
#     return total


def total_spending_by_category():
    total = 0
    found = False
    choose = input("Please enter the category: ")
    formatted = choose.lower().strip()

    if EXPENSES_FILE.exists():
        with EXPENSES_FILE.open("r") as f:
            expenses = f.readlines()
            print(f"\n🔍 Total spend by category: {formatted}")

            for e in expenses:
                parts = e.strip().split("|")
                if len(parts) < 2:
                    continue  # skip invalid lines

                categ = parts[1].strip().lower()
                if categ == formatted:
                    try:
                        amount = float(parts[0].strip())
                        total += amount
                        found = True
                    except ValueError:
                        print(f"❌ Skipping invalid amount in: {e.strip()}")

    if found:
        print(f"✅ Total spend for '{formatted}': ₹{total}")
    else:
        print(f"⚠️ No expenses found under category '{formatted}'")

    return total
