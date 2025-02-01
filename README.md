# SIEM Suspicious Activity Monitoring Dashboard

## Overview

This project implements a **Security Information and Event Management (SIEM) dashboard** using **Flask and MongoDB** to display suspicious activity logs detected from audit logs. The system identifies security threats and provides a **web interface** for monitoring alerts.

## Features

- 🚀 **Real-time Monitoring** of suspicious activities in audit logs.
- 🛠 **Detection of Suspicious Commands** (e.g., `wget`, `curl`, `iptables`).
- 📊 **Web-Based Dashboard** for viewing alerts.
- 📡 **MongoDB Storage** for logs and alerts.
- 🔔 **Automated Alert Generation** for suspicious activities.

## Project Structure

```
📂 siem_dashboard/
├── 📂 templates/             # HTML Templates for Flask
│   ├── index.html           # Main Dashboard Page
├── audit_log_to_mongodb.py   # Parses Linux audit logs and stores them in MongoDB
├── detect_suspicious_activity.py # Detects suspicious activities and generates alerts
├── flask_audit_dashboard.py  # Flask Web Application
├── requirements.txt          # Python Dependencies
├── README.md                 # Project Documentation
```

## Setup Instructions

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/Hariharan-2411/SIEM-Dashboard.git
cd SIEM-Dashboard
```

### 2️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 3️⃣ Run MongoDB (Ensure MongoDB is Running)

```sh
sudo systemctl start mongod  # For Linux
net start MongoDB            # For Windows
```

### 4️⃣ Run the Flask Application

```sh
python flask_audit_dashboard.py
```

### 5️⃣ Open the Dashboard in Your Browser

Visit [**http://127.0.0.1:5000/**](http://127.0.0.1:5000/) to view the Suspicious Activity Logs.

## How It Works

1. `` extracts suspicious logs from `/var/log/audit/audit.log` and stores them in MongoDB.
2. `` scans MongoDB for **suspicious commands and high CPU usage** and generates alerts.
3. `` runs a **Flask web server** that retrieves alerts and displays them in the dashboard.

## Technologies Used

- **Python** (Flask, PyMongo)
- **MongoDB** (Log Storage)
- **HTML/CSS** (Front-end Dashboard)

## Future Enhancements

- ✅ Implement **User Authentication** for Secure Access.
- ✅ Add **Real-time Log Streaming**.
- ✅ Integrate with **External Threat Feeds**.

## License

This project is open-source and available under the **MIT License**.

## Contact

For any questions or issues, please contact **Hariharan** at [GitHub](https://github.com/Hariharan-2411).

