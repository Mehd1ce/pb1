import json
import time

journal_entries = []

def recursive_count(entries):
    return 0 if not entries else 1 + recursive_count(entries[1:])

def welcome_screen():
    print("="*50)
    print("       WELCOME TO DAILY JOURNAL APP")
    print("="*50)
    for i in range(3):
        print("Loading" + "."*(i+1))
        time.sleep(0.3)

def show_menu():
    print("\nMain Menu:")
    print("1. Add New Entry")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Update Entry")
    print("5. Delete Entry")
    print("6. Summary Stats")
    print("7. Save to File")
    print("8. Load from File")
    print("9. Sort Entries")
    print("10. Help")
    print("11. Clear All Data")
    print("12. Exit")

def add_entry():
    try:
        entry_id = input("Entry ID: ")
        date = input("Date (YYYY-MM-DD): ")
        title = input("Title: ")
        content = input("Content: ")
        mood = input("Mood (Happy, Sad, etc.): ")
        journal_entries.append({"id": entry_id, "date": date, "title": title, "content": content, "mood": mood})
        print("Entry added.")
    except Exception as e:
        print(f"Error adding entry: {e}")

def view_entries():
    if not journal_entries:
        print("No entries found.")
    else:
        for e in journal_entries:
            print(f"ID: {e['id']} | Date: {e['date']} | Title: {e['title']} | Mood: {e['mood']}\nContent: {e['content']}\n")

def search_entry():
    keyword = input("Search by ID or Title: ")
    found = [e for e in journal_entries if e['id'] == keyword or e['title'].lower() == keyword.lower()]
    if found:
        for e in found:
            print(e)
    else:
        print("Entry not found.")

def update_entry():
    eid = input("Enter ID of entry to update: ")
    for e in journal_entries:
        if e['id'] == eid:
            e['title'] = input("New Title: ")
            e['content'] = input("New Content: ")
            e['mood'] = input("New Mood: ")
            print("Entry updated.")
            return
    print("Entry not found.")

def delete_entry():
    eid = input("Enter ID to delete: ")
    global journal_entries
    journal_entries = [e for e in journal_entries if e['id'] != eid]
    print("Entry deleted if existed.")

def summary_stats():
    print(f"Total Entries: {len(journal_entries)}")
    print(f"Recursive Count: {recursive_count(journal_entries)}")

def save_file():
    with open("journal_entries.json", "w") as f:
        json.dump(journal_entries, f)
    print("Saved to file.")

def load_file():
    global journal_entries
    try:
        with open("journal_entries.json", "r") as f:
            journal_entries = json.load(f)
        print("Loaded from file.")
    except FileNotFoundError:
        print("File not found.")

def sort_entries():
    key = input("Sort by (id/date/title/mood): ")
    if key in ["id", "date", "title", "mood"]:
        journal_entries.sort(key=lambda x: x[key])
        print("Entries sorted.")
    else:
        print("Invalid sort key.")

def help_info():
    print("Daily Journal App allows you to record your daily experiences.")
    print("Use options to add, view, search, edit, delete, and save entries.")

def clear_all():
    confirm = input("Type YES to confirm clearing all data: ")
    if confirm == "YES":
        journal_entries.clear()
        print("All entries cleared.")
    else:
        print("Clear cancelled.")

def main():
    welcome_screen()
    while True:
        show_menu()
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                add_entry()
            elif choice == 2:
                view_entries()
            elif choice == 3:
                search_entry()
            elif choice == 4:
                update_entry()
            elif choice == 5:
                delete_entry()
            elif choice == 6:
                summary_stats()
            elif choice == 7:
                save_file()
            elif choice == 8:
                load_file()
            elif choice == 9:
                sort_entries()
            elif choice == 10:
                help_info()
            elif choice == 11:
                clear_all()
            elif choice == 12:
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
