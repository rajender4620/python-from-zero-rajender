import json
from pathlib import Path
from datetime import datetime

NOTES_FILE = Path("smart-life-manager/notes/notes.json")

def load_notes():
    if NOTES_FILE.exists():
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note():
    title = input("Enter title: ").strip()
    content = input("Enter content: ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    note = {"title": title, "content": content, "timestamp": timestamp}
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("✅ Note added.")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes yet.")
        return
    print("\n🗒️ Notes:")
    for i, note in enumerate(notes):
        print(f"{i}. {note['title']} ({note['timestamp']})")

def view_note():
    notes = load_notes()
    list_notes()
    try:
        idx = int(input("Enter note index to view: "))
        note = notes[idx]
        print(f"\n📄 {note['title']}\n{note['content']}")
    except (ValueError, IndexError):
        print("❌ Invalid index.")

def delete_note():
    notes = load_notes()
    list_notes()
    try:
        idx = int(input("Enter note index to delete: "))
        removed = notes.pop(idx)
        save_notes(notes)
        print(f"🗑️ Deleted note: {removed['title']}")
    except (ValueError, IndexError):
        print("❌ Invalid index.")

def update_note():
    notes = load_notes()
    list_notes()
    try:
        idx = int(input("Enter note index to update: "))
        note = notes[idx]

        new_title = input(f"New title (or press Enter to keep '{note['title']}'): ").strip()
        new_content = input(f"New content (or press Enter to keep existing content): ").strip()

        if new_title:
            note["title"] = new_title
        if new_content:
            note["content"] = new_content

        save_notes(notes)
        print("✏️ Note updated.")
    except (ValueError, IndexError):
        print("❌ Invalid index.")
