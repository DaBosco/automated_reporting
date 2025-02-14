import smtplib
import os
from email.message import EmailMessage

EMAIL_SENDER = "put-here-your-email"
EMAIL_PASSWORD = "xxxx xxxx xxxx xxxx" #Generate an App Password by going to Google Account Security, enabling Two-Factor Authentication (if not already active), scrolling to "App Passwords," clicking "Generate a new password," selecting "Mail" and "Windows Computer," then clicking "Generate" and copying the 16-character code provided (e.g., abcd efgh ijkl mnop).
EMAIL_RECEIVER = "put-here-your-email"

import os

base_dir = os.path.dirname(os.path.abspath(__file__))  
csv_path = os.path.join(base_dir, "../data/sales_report.csv")  
csv_path = os.path.abspath(csv_path)


msg = EmailMessage()
msg["Subject"] = "📊 Daily Report"
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER
msg.set_content("Hello,\nattached you will find the daily sales report.\n\nBest regards!")

with open(csv_path, "rb") as file:
    msg.add_attachment(file.read(), maintype="text", subtype="csv", filename=os.path.basename(csv_path))

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        print("✅ Email sent successfully!")
except Exception as e:
    print(f"❌ Error sending the email: {e}")

