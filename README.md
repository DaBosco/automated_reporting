# Automated Reporting System

## 📌 Project Overview
This project automates the generation of sales reports from a MariaDB database, formats them into CSV files, and sends them via email. The system is built using Python, MariaDB, and Metabase, with automation handled through cron jobs.

## 🛠️ Technologies Used
- **Python** (for data processing and email automation)
- **MariaDB** (database for storing sales data)
- **Metabase** (for dashboard visualization)
- **Linux Cron Jobs** (for scheduled automation)

## 🚀 Features
- Connects to a MariaDB database
- Extracts sales data and saves it as a CSV report
- Sends the report via email
- Runs automatically at scheduled intervals using cron jobs

## 📂 Project Structure
```
.
├── cronjob.sh                  # Shell script to execute the automation
├── data
│   └── sales_report.csv        # Generated sales report
├── logs
│   └── cron.log                # Log file for cron job execution
├── scripts
│   ├── generate_report.py      # Extracts sales data and saves as CSV
│   ├── send_email.py           # Sends the CSV report via email
├── myenv                       # Python virtual environment
├── dashboard                   # (Optional) Metabase dashboard setup
└── README.md                   # Project documentation
```

## 🛠️ Setup Instructions
### 1️⃣ Install Dependencies
Ensure you have Python and MariaDB installed. Then, install the required Python packages:
```bash
pip install -r requirements.txt
```

### 2️⃣ Configure Database Connection
Edit `scripts/generate_report.py` with your MariaDB credentials:
```python
conn = pymysql.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="reports_db"
)
```

### 3️⃣ Set Up Cron Job (Automation)
Open the cron job editor:
```bash
crontab -e
```
Add the following line to schedule the report generation and email sending every day at 8 AM:
```bash
0 8 * * * /path/to/automated_reporting/cronjob.sh >> /path/to/automated_reporting/logs/cron.log 2>&1
```

### 4️⃣ Run Manually (For Testing)
You can manually generate and send a report:
```bash
python3 scripts/generate_report.py
python3 scripts/send_email.py
```

## 📧 Email Configuration
Modify `scripts/send_email.py` with your SMTP credentials (e.g., Gmail SMTP):
```python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
```
For Gmail, you may need to generate an **App Password** instead of using your main password.

## 🔥 Future Improvements
- Add error handling and logging for debugging
- Implement a web dashboard with Metabase for report visualization
- Enhance security for email authentication (OAuth)

## 📜 License
This project is licensed under the MIT License.
