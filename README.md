# synent-task3-todolist-Dharshini
# ✅ To-Do List Manager

A persistent terminal-based task manager that saves your tasks to a JSON file.

## Features
- Add new tasks with today's date
- View all tasks — pending and completed
- Mark tasks as complete (records completion date)
- Delete individual tasks
- Clear all completed tasks at once
- Data saved to `tasks.json` — persists after closing the app
- Shows total pending vs completed count

## Requirements
```bash
pip install colorama
```

## How to Run
```bash
python todo.py
```

## How to Use
1. Run the program — existing tasks load automatically
2. Choose from the menu:
   - **1** — View all tasks
   - **2** — Add a new task
   - **3** — Mark a task as complete
   - **4** — Delete a task
   - **5** — Clear all completed tasks
   - **6** — Exit

## Data Storage
Tasks are saved in `tasks.json` in the same folder. The file is created automatically on first run.

## Technologies Used
- Python 3
- `json` — persistent task storage
- `datetime` — timestamps for tasks
- `colorama` — colored terminal output

## Authors
Dharshini | Synent Technologies Internship 2026
