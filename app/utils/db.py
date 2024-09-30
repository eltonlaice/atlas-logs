from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# MongoDB connection settings
MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME')

# Create a MongoDB client
client = MongoClient(MONGO_URI)

# Get the database
db = client[DB_NAME]

# Get the audit_logs collection
audit_logs = db.audit_logs

# Create a text index on the message field for text search
audit_logs.create_index([('message', 'text')])

# Create an index on the timestamp field for efficient date-based queries
audit_logs.create_index('timestamp')

class AuditLog:
    def __init__(self, message, level="INFO", server=None):
        self.timestamp = datetime.utcnow()
        self.level = level
        self.message = message
        self.server = server

    def save(self):
        log_entry = {
            "timestamp": self.timestamp,
            "level": self.level,
            "message": self.message,
            "server": self.server
        }
        result = audit_logs.insert_one(log_entry)
        return str(result.inserted_id)

    @staticmethod
    def query(query=None, start_date=None, end_date=None, server=None, limit=100):
        filter_criteria = {}

        if query:
            filter_criteria["$text"] = {"$search": query}

        if start_date or end_date:
            date_filter = {}
            if start_date:
                date_filter["$gte"] = start_date
            if end_date:
                date_filter["$lte"] = end_date
            filter_criteria["timestamp"] = date_filter

        if server:
            filter_criteria["server"] = server

        cursor = audit_logs.find(filter_criteria).sort("timestamp", -1).limit(limit)
        return [AuditLog.from_dict(log) for log in cursor]

    @classmethod
    def from_dict(cls, log_dict):
        log = cls(log_dict['message'], log_dict['level'], log_dict['server'])
        log.timestamp = log_dict['timestamp']
        return log


