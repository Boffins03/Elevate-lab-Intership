#  To-Do List Manager

This is a simple **command-line To-Do List Manager** written in Python.  
It allows users to **view tasks, add new tasks, remove completed tasks, and save tasks persistently** in a text file.

---

##  Why I Built It This Way

1. **File Persistence with `tasks.txt`**
   - I used a text file (`tasks.txt`) to store tasks so that tasks are **not lost after the program is closed**.
   - Chose a plain text file instead of a database to keep the project **lightweight and beginner-friendly**.

2. **Functions for Modular Design**
   - Each action (`add_task`, `remove_task`, `view_tasks`, `save_tasks`, `load_tasks`) is placed in a **separate function**.
   - This makes the code **organized, reusable, and easier to maintain**.

3. **Error Handling**
   - `FileNotFoundError` is handled in `load_tasks` so the program still works even if `tasks.txt` doesn’t exist.
   - `ValueError` and invalid index checks prevent the program from crashing when a user enters the wrong input.

4. **User-Friendly Menu**
   - A clear text-based menu guides the user step by step.
   - After each action, the program **confirms the operation** (e.g., “Task added.” or “Removed: task_name”).

5. **Simple, Beginner-Friendly Approach**
   - I avoided external libraries to keep it **pure Python** and easy to understand.
   - Focused on **basic file handling, lists, and loops**, which are essential for learning Python.

---

##  Features
- View all tasks
- Add new tasks
- Remove tasks by selecting task number
- Persistent storage in `tasks.txt`

---

##  How to Run
1. Clone this repository or copy the code into a file called `todo.py`.
2. Run the program:
   ```bash
   python todo.py
