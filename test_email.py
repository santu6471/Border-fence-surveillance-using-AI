# test_email.py
import os, smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

smtp_host = os.getenv("ALERT_EMAIL_SMTP_HOST", "smtp.gmail.com")
smtp_port = int(os.getenv("ALERT_EMAIL_SMTP_PORT", 587))
user = os.getenv("ALERT_EMAIL_FROM")
password = os.getenv("ALERT_EMAIL_PASSWORD")
to = [e.strip() for e in os.getenv("ALERT_EMAIL_TO","").split(",") if e.strip()]

msg = EmailMessage()
msg["From"] = user
msg["To"] = ", ".join(to)
msg["Subject"] = "Test alert email"
msg.set_content("This is a test email from SkySentinel.")

try:
    with smtplib.SMTP(smtp_host, smtp_port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(msg)
    print("Email sent OK to", to)
except Exception as e:
    print("Email failed:", e)
