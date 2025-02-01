import pymongo
from pymongo import MongoClient
from bson import ObjectId  


# MongoDB client connection
client = MongoClient("mongodb://localhost:27017/")
db = client['audit_logs_db']
collection = db['audit_logs']


log_file_path = "/var/log/audit/audit.log" # For linux


def extract_value(log_line, key):
    start_index = log_line.find(key+ "=")
    end1 = len(log_line)
    if start_index == -1 :
        return None
    count = 0
    for i in range (start_index,end1):
        count = count +1
        if log_line[i]  == " ":
            break;
    start = start_index + len(key)+1
    return log_line[start : (start_index+count)].strip()


def parse_log(log):
    log_dict = {
    "_id": ObjectId(),  
    "type": None,
    "msg": None,
    "proctitle": None,
    "comm": None,
    "pid": None,
    "exe": None,
    "uid": None,
    "euid": None
    }


    # Parse fields using the helper function
    log_dict["type"] = extract_value(log, "type")
    log_dict["msg"] = extract_value(log, "msg").split("(")[1].split(")")[0] if extract_value(log, "msg") else None
    log_dict["proctitle"] = extract_value(log, "proctitle")
    log_dict["comm"] = extract_value(log, "comm").strip('"') if extract_value(log, "comm") else None
    log_dict["pid"] = extract_value(log, "pid")
    log_dict["exe"] = extract_value(log, "exe").strip('"') if extract_value(log, "exe") else None
    log_dict["uid"] = extract_value(log, "uid")
    log_dict["euid"] = extract_value(log, "euid")

    return log_dict



def process_audit_logs():
    try:
        with open(log_file_path, "r") as log_file:
            for line in log_file:
                parsed_log = parse_log(line.strip())
                if parsed_log:
                    collection.insert_one(parsed_log)
                    print(f"Log inserted: {parsed_log}")
                else:
                    print("Failed to parse log:", line.strip())
    except FileNotFoundError:
        print(f"Log file not found: {log_file_path}")
    except Exception as e:
        print(f"Eroor reading log file: {e}")

process_audit_logs()

client.close()

