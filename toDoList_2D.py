print("Life Organizer")
print()
toDolist = []

def add():
    item = input("What do you want to add to the list?: ")
    due = input("When is it due?: ")
    priority = input("What is the priority?: ")
    row = [item, due, priority]
    toDolist.append(row)
    print("Added to list")

def view():
    view_choice = input("1: View All\n2: View By Priority\n> ")
    if view_choice == "1":
        for row in toDolist:
            print(" | ".join(row))
    elif view_choice == "2":
        priority = input("What priority?: ")
        for row in toDolist:
            if row[2] == priority:
                print(" | ".join(row))
    print()

def edit():
    find = input("Name of to-do to edit > ")
    found = False
    for row in toDolist:
        if find == row[0]:  # Match by name
            found = True
            toDolist.remove(row)
            name = input("New Name > ")
            date = input("New Due Date > ")
            priority = input("New Priority > ").capitalize()
            row = [name, date, priority]
            toDolist.append(row)
            print("Item updated")
            break
    if not found:
        print("Couldn't find that item")

def remove():
    find = input("Name of to-do to remove > ")
    for row in toDolist:
        if find == row[0]:  # Match by name
            toDolist.remove(row)
            print("Item removed")
            break
    else:
        print("Couldn't find that item")

while True:
    menu = input("Do you want to view, add, edit, or remove a to-do list item? > ").lower()
    if menu == "view":
        view()
    elif menu == "add":
        add()
    elif menu == "edit":
        edit()
    elif menu == "remove":
        remove()
    else:
        print("Invalid choice. Please enter 'view', 'add', 'edit', or 'remove'.")
