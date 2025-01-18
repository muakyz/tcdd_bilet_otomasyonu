import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()
gmail_user = os.getenv("gmail_user")
gmail_password = os.getenv("gmail_password")
to_email = os.getenv("to_email")
subject = os.getenv("subject")
body = os.getenv("body")

message = MIMEMultipart()
message['From'] = gmail_user
message['To'] = to_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

def send_mail():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_password)

        server.sendmail(gmail_user, to_email, message.as_string())
        print("E-posta başarıyla gönderildi!")
    except Exception as e:
        print(f"Hata oluştu: {e}")
    finally:
        server.quit()
