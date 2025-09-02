# todo.py

# Step 1: Start with an empty list to hold tasks
tasks = []
# Step 2: Add a task
def add_task(task):
    tasks.append(task)

# Step 3: View tasks

def view_tasks():
    if not tasks:
        print("No tasks.")
    for i, task in enumerate(tasks):
        print(f"{i}: {task}")

# Step 4: Delete a task


# Step 5: Mark task complete

def mark_complete(index):
    if 0 <= index < len(tasks):
        tasks[index] += " (complete)"
    else:
        print("Invalid task index.")


# Step 6: Save/load tasks (extra stretch for today)

def save_tasks(filename="tasks.txt"):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task + "\n")


# Demo flow (you can run this file directly: python todo.py)
if __name__ == "__main__":
    add_task("Finish Cyber 201 assignment")
    add_task("Push code to GitHub")
    add_task(input("Enter a new task: "))
    view_tasks()
    mark_complete(0)
    view_tasks()
    save_tasks()