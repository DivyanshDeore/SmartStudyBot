from database import task_collection

def add_task(task, deadline):
    task_collection.insert_one({
        "task": task,
        "deadline": deadline,
        "status": "pending"
    })
    return "✅ Task added successfully."

def get_tasks():
    tasks = list(task_collection.find({}, {"_id": 0}))
    if not tasks:
        return "No pending tasks."

    result = "📌 Your Tasks:\n"
    for t in tasks:
        result += f"- {t['task']} (Deadline: {t['deadline']})\n"

    return result