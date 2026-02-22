import random
from database import chat_collection
from reminder import add_task, get_tasks
from scheduler import create_schedule

motivations = [
    "🔥 Small progress every day leads to big success.",
    "📘 Discipline beats motivation.",
    "🚀 Your future self will thank you for studying today.",
    "💪 Stay consistent, success is coming."
]

def save_chat(user, bot):
    chat_collection.insert_one({
        "user": user,
        "bot": bot
    })

def get_response(message):

    msg = message.lower()

    # ---- ADD TASK ----
    if "add assignment" in msg:
        try:
            parts = message.split("|")
            task = parts[1]
            deadline = parts[2]
            reply = add_task(task, deadline)
        except:
            reply = "Use format: add assignment | task | deadline"

    # ---- SHOW TASKS ----
    elif "show assignments" in msg or "tasks" in msg:
        reply = get_tasks()

    # ---- STUDY SCHEDULE ----
    elif "schedule" in msg:
        reply = create_schedule("Math, Java, DSA, English", 2)

    # ---- MOTIVATION ----
    elif "motivate" in msg or "lazy" in msg:
        reply = random.choice(motivations)

    # ---- STUDY QUESTIONS (DEFAULT CHATBOT) ----
    else:
        reply = (
            "📚 I'm your Smart Study Bot.\n"
            "You can ask:\n"
            "- add assignment | task | deadline\n"
            "- show assignments\n"
            "- make schedule\n"
            "- motivate me"
        )

    save_chat(message, reply)

    return reply