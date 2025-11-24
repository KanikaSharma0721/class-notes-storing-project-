import os

NOTE_DIR = "class_notes"

def setup_notebook():
    if not os.path.exists(NOTE_DIR):
        os.makedirs(NOTE_DIR)
        print(f"Created directory: {NOTE_DIR}")

def list_notes():
    print("\n--- Available Notes ---")
    notes = os.listdir(NOTE_DIR)
    if not notes:
        print("No notes found.")
    for note in notes:
        print(f"- {note.replace('.txt', '')}")
    print("-----------------------\n")

def view_note(title):
    path = os.path.join(NOTE_DIR, f"{title}.txt")
    if os.path.exists(path):
        with open(path, 'r') as f:
            print(f"\n--- {title} ---\n")
            print(f.read())
            print(f"\n--- End of Note ---\n")
    else:
        print(f"Error: Note '{title}' not found.")

def create_note(title, content):
    path = os.path.join(NOTE_DIR, f"{title}.txt")
    try:
        with open(path, 'w') as f:
            f.write(content)
        print(f"Note '{title}' saved successfully.")
    except IOError as e:
        print(f"Error saving note: {e}")

def delete_note(title):
    path = os.path.join(NOTE_DIR, f"{title}.txt")
    if os.path.exists(path):
        os.remove(path)
        print(f"Note '{title}' deleted.")
    else:
        print(f"Error: Note '{title}' not found.")

def main_menu():
    setup_notebook()
    while True:
        print("\nDigital Notebook Menu:")
        print("1. Create/Edit a note")
        print("2. View a note")
        print("3. List all notes")
        print("4. Delete a note")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter note title: ")
            content = input("Enter note content (Ctrl+D or Ctrl+Z on Windows when done): ")
            create_note(title, content)
        elif choice == '2':
            title = input("Enter the title of the note to view: ")
            view_note(title)
        elif choice == '3':
            list_notes()
        elif choice == '4':
            title = input("Enter the title of the note to delete: ")
            delete_note(title)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()