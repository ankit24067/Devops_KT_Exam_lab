import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_alert_email(message: str):

    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    receiver = os.getenv("EMAIL_RECEIVER")

    msg = MIMEText(message)
    msg["Subject"] = "KT Exam Alert"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        print("Alert email sent successfully")
    except Exception as e:
        print("Email sending failed:", e)
