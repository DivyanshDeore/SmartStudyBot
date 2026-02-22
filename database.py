from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client["smartstudybot"]

chat_collection = db["chats"]
task_collection = db["tasks"]

print("✅ MongoDB Connected")