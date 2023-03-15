import smtplib
import ssl
import os
from dotenv import load_dotenv


def send_email(message):
    load_dotenv()
    host = 'smtp.gmail.com'
    port = 465
    username = os.getenv('EMAIL_FROM')
    password = os.getenv('PASSWORD')
    receiver = os.getenv('EMAIL_TO')
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
