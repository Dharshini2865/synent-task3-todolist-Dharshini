# Task 3: To-Do List Manager
# Synent Technologies Python Internship
# Features: Add, view, complete, delete tasks — saved to JSON file

import json
import os
from datetime import datetime
from colorama import init, Fore, Style
init(autoreset=True)

FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file — returns empty list if file doesn't exist"""
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Save all tasks to JSON file so data persists after closing"""
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show_banner():
    print(Fore.CYAN + "=" * 52)
    print(Fore.CYAN + "      TO-DO LIST MANAGER — Synent Internship")
    print(Fore.CYAN + "=" * 52)


def show_tasks(tasks):
    """Display all tasks with numbering and status"""
    print()
    if not tasks:
        print(Fore.YELLOW + "  No tasks yet! Add one from the menu.")
        return

    done   = [t for t in tasks if t["done"]]
    undone = [t for t in tasks if not t["done"]]

    print(Fore.WHITE + f"  Tasks: {len(undone)} pending, {len(done)} completed\n")

    for i, task in enumerate(tasks, 1):
        if task["done"]:
            status = Fore.GREEN + "  [✓]"
            title  = Fore.GREEN + Style.DIM + f" {i}. {task['title']}"
            date   = Fore.GREEN + Style.DIM + f"  (done {task['done_at']})"
        else:
            status = Fore.YELLOW + "  [ ]"
            title  = Fore.WHITE  + f" {i}. {task['title']}"
            date   = Fore.WHITE  + Style.DIM + f"  (added {task['created']})"

        print(status + title + date)

    print()


def add_task(tasks):
    """Add a new task"""
    print()
    title = input(Fore.YELLOW + "  Task name: ").strip()
    if not title:
        print(Fore.RED + "  Task name cannot be empty!")
        return tasks

    task = {
        "title":   title,
        "done":    False,
        "created": datetime.now().strftime("%d %b %Y"),
        "done_at": None
    }
    tasks.append(task)
    save_tasks(tasks)
    print(Fore.GREEN + f"  ✓ Task added: \"{title}\"")
    return tasks


def complete_task(tasks):
    """Mark a task as completed"""
    show_tasks(tasks)
    if not tasks:
        return tasks

    pending = [t for t in tasks if not t["done"]]
    if not pending:
        print(Fore.YELLOW + "  All tasks are already completed!")
        return tasks

    try:
        num = int(input(Fore.YELLOW + "  Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            if tasks[num - 1]["done"]:
                print(Fore.YELLOW + "  This task is already completed.")
            else:
                tasks[num - 1]["done"]    = True
                tasks[num - 1]["done_at"] = datetime.now().strftime("%d %b %Y")
                save_tasks(tasks)
                print(Fore.GREEN + f"  ✓ Completed: \"{tasks[num - 1]['title']}\"")
        else:
            print(Fore.RED + "  Invalid task number!")
    except ValueError:
        print(Fore.RED + "  Please enter a number!")
    return tasks


def delete_task(tasks):
    """Delete a task permanently"""
    show_tasks(tasks)
    if not tasks:
        return tasks

    try:
        num = int(input(Fore.YELLOW + "  Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(Fore.GREEN + f"  ✓ Deleted: \"{removed['title']}\"")
        else:
            print(Fore.RED + "  Invalid task number!")
    except ValueError:
        print(Fore.RED + "  Please enter a number!")
    return tasks


def clear_completed(tasks):
    """Remove all completed tasks at once"""
    before = len(tasks)
    tasks  = [t for t in tasks if not t["done"]]
    removed = before - len(tasks)
    save_tasks(tasks)
    if removed:
        print(Fore.GREEN + f"  ✓ Cleared {removed} completed task(s).")
    else:
        print(Fore.YELLOW + "  No completed tasks to clear.")
    return tasks


def show_menu():
    print(Fore.CYAN  + "\n  MENU")
    print(Fore.GREEN + "  1. View all tasks")
    print(Fore.GREEN + "  2. Add a task")
    print(Fore.GREEN + "  3. Mark task as complete")
    print(Fore.GREEN + "  4. Delete a task")
    print(Fore.GREEN + "  5. Clear all completed tasks")
    print(Fore.RED   + "  6. Exit")
    print()


def main():
    show_banner()
    tasks = load_tasks()
    print(Fore.CYAN + f"\n  Loaded {len(tasks)} task(s) from file.")

    while True:
        show_menu()
        choice = input(Fore.YELLOW + "  Enter choice (1-6): ").strip()

        if   choice == "1": show_tasks(tasks)
        elif choice == "2": tasks = add_task(tasks)
        elif choice == "3": tasks = complete_task(tasks)
        elif choice == "4": tasks = delete_task(tasks)
        elif choice == "5": tasks = clear_completed(tasks)
        elif choice == "6":
            print(Fore.CYAN + f"\n  Saved {len(tasks)} task(s). Goodbye!\n")
            break
        else:
            print(Fore.RED + "  Please enter a number from 1 to 6.")

        print(Fore.CYAN + "  " + "-" * 48)


if __name__ == "__main__":
    main()
