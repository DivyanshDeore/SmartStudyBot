📚 Smart Study Bot — AI Study Assistant

🚀 Project Overview

Smart Study Bot is an AI-powered study assistant designed to help students manage their academic life efficiently.
The chatbot assists students by organizing assignments, generating study schedules, providing motivational support, and maintaining conversation history using a database.

The system is built using FastAPI, Python, and MongoDB, and works as a backend API that simulates a personal academic assistant.

This project demonstrates how modern AI assistants maintain context, store user data, and automate productivity tasks for students.

---

🎯 Problem Statement

Students often struggle with:

- Remembering assignment deadlines
- Maintaining consistent study schedules
- Staying motivated during study sessions
- Managing multiple subjects effectively

Smart Study Bot solves these problems by acting as a personal study companion that provides reminders, planning assistance, and motivational interaction.

---

✨ Features

✅ Assignment Reminder System

- Add assignments with deadlines
- Store tasks permanently in MongoDB
- View all pending assignments anytime

✅ Study Schedule Generator

- Automatically creates study plans
- Distributes subjects across time slots
- Helps maintain balanced study routines

✅ Motivation Assistant

- Provides motivational messages
- Encourages discipline and consistency
- Helps students overcome procrastination

✅ Chat Memory (Database Storage)

- Stores conversations in MongoDB
- Maintains interaction history
- Demonstrates persistent chatbot memory

✅ REST API Backend

- Built using FastAPI
- Interactive API testing via Swagger UI
- Ready for deployment

---

🧠 System Architecture

User → FastAPI Server → Chatbot Logic → MongoDB Database → Response to User

1. User sends a message through API.
2. FastAPI receives request.
3. Chatbot logic processes user intent.
4. Data is stored/retrieved from MongoDB.
5. Response is returned to the user.

---

🛠️ Tech Stack

Technology| Purpose
Python| Core programming language
FastAPI| Backend API framework
MongoDB Atlas| Database for storing chats & tasks
PyMongo| MongoDB connection
Uvicorn| ASGI server
dotenv| Environment variable management

---

📁 Project Structure

SmartStudyBot/
│
├── main.py           # FastAPI server
├── chatbot.py        # Main chatbot logic
├── database.py       # MongoDB connection
├── reminder.py       # Assignment management
├── scheduler.py      # Study schedule generator
├── requirements.txt  # Dependencies
├── .env              # Environment variables (not uploaded)
└── README.md

---

⚙️ Installation & Setup

1️⃣ Clone Repository

git clone https://github.com/yourusername/SmartStudyBot.git
cd SmartStudyBot

---

2️⃣ Create Virtual Environment

python -m venv venv

Activate:

Windows

venv\Scripts\activate

---

3️⃣ Install Dependencies

pip install -r requirements.txt

---

4️⃣ Setup Environment Variables

Create ".env" file:

MONGO_URL=your_mongodb_connection_string

---

5️⃣ Run Application

uvicorn main:app --reload

Open browser:

http://127.0.0.1:8000/docs

---

💬 API Usage Examples

Add Assignment

add assignment | Java Project | 25 Feb

Show Assignments

show assignments

Generate Study Schedule

make schedule

Motivation

motivate me

---

🗄️ Database Design

Chats Collection

Stores chatbot conversations:

{
  "user": "message",
  "bot": "response"
}

Tasks Collection

Stores assignments:

{
  "task": "Java Project",
  "deadline": "25 Feb",
  "status": "pending"
}

---

🔍 Testing

The API can be tested using:

- FastAPI Swagger UI ("/docs")
- Postman
- Browser API interface

---

🚀 Future Improvements

- Integration with real AI LLM APIs
- Automatic deadline notifications
- Email or WhatsApp reminders
- Frontend chat interface
- Voice-enabled study assistant
- Personalized AI study planning

---

🎓 Learning Outcomes

Through this project, the following concepts were implemented:

- REST API development
- Database integration
- Backend architecture design
- Chatbot logic implementation
- Persistent memory systems
- API deployment workflow

---

👨‍💻 Author

Divyansh Deore
Smart Study Bot Project

---

📄 License

This project is created for educational and academic purposes.
