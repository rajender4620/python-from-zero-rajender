import json
from pathlib import Path

CONTACT_FILE = Path("smart-life-manager/contacts/contacts.json")


def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=2)


def load_contacts():
    if CONTACT_FILE.exists():
        with open(CONTACT_FILE, "r") as f:
            return json.load(f)
    return []


def add_contacts():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    contact = {"name": name, "phone": phone, "email": email}

    contacts = load_contacts()     # ✅ this returns a list
    contacts.append(contact)       # ✅ appending dict to list
    save_contacts(contacts)        # ✅ dumping the updated list


def list_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts yet.")
        return

    print("\n📇 Contact List:")
    for i, c in enumerate(contacts):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")


def delete_contact():
    contacts = load_contacts()
    list_contacts()
    try:
        idx = int(input("Enter contact index to delete: "))
        removed = contacts.pop(idx)
        save_contacts(contacts)
        print(f"🗑️ Deleted: {removed['name']}")
    except (ValueError, IndexError):
        print("❌ Invalid index.")
