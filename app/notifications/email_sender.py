import smtplib
from email.mime.text import MIMEText
from app.config import *

def send_email(content):

    try:

        msg = MIMEText(content)

        msg["Subject"] = "Daily News Digest"
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_USER

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            EMAIL_USER,
            EMAIL_PASSWORD
        )

        server.send_message(msg)

        server.quit()

        print("Email Sent Successfully")

    except Exception as e:

        print("Email Error:", str(e))