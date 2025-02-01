import pymongo
from pymongo import MongoClient
from bson import ObjectId

# MongoDB client connection
client = MongoClient("mongodb://localhost:27017/")
db = client['audit_logs_db']

collection = db['audit_logs']
alert_collection = db['alerts']

# detect suspicious activities
def detection_and_alerting():
    suspicious_commands = collection.find({"comm": {"$in": ["wget", "curl","iptables"]}})
    for log in suspicious_commands:
        print(f"Suspicious activity detected: {log['comm']}")
        generate_alert(log)

    # Detect high CPU usage or unusual process execution
    high_cpu_usage = collection.find({"pid": {"$in": ["34150", "1234", "5678", "9012"]}})  # Example PIDs
    for log in high_cpu_usage:
        print(f"High CPU usage detected: {log}")
        generate_alert(log)

# Function to generate alerts
def generate_alert(log):
    
    alert = {
        "timestamp": log.get("timestamp", ObjectId()),  
        "message": f"Suspicious activity detected by user {log.get('uid', 'Unknown')}",
        "details": log
    }
    alert_collection.insert_one(alert)
    print(f"Alert generated for log: {log['_id']}")

detection_and_alerting()
client.close()
