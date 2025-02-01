from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client['audit_logs_db']
alert_collection = db['alerts']

# Route to Display Suspicious Logs
@app.route('/')
def index():
    logs = list(alert_collection.find().sort("_id", -1))  # Fetch & sort logs (latest first)
    return render_template('index.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
