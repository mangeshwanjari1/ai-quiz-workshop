
import os
import smtplib
import ssl
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "AI Quiz Workshop - Test Email"
msg["From"] = os.environ["SMTP_FROM"]
msg["To"] = input("Enter recipient email: ").strip()
msg.set_content("This is a test email from Module 5.")

try:
    with smtplib.SMTP_SSL(
        os.environ["SMTP_HOST"],
        int(os.environ.get("SMTP_PORT", "465")),
        context=ssl.create_default_context()
    ) as smtp:
        smtp.login(
            os.environ["SMTP_USER"],
            os.environ["SMTP_PASSWORD"]
        )
        smtp.send_message(msg)

    print("Email accepted by SMTP server.")

except Exception as e:
    print("Email sending failed:", e)
