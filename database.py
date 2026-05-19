import os
from pymongo import MongoClient
from dotenv import load_dotenv

import certifi

# Load environment variables from a .env file if it exists
load_dotenv()

# Get MongoDB URI from environment or default to localhost for development
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("MONGO_DB_NAME", "attendance_db")

# Use certifi to prevent SSL handshake errors on minimal cloud environments like Render
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client[DB_NAME]

def get_db():
    return db
