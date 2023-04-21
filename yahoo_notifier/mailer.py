import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

class Mailer:

    def __init__(self):
        self.smtp_server: str = os.getenv('SMTP_SERVER') 
        self.smtp_port: int = os.getenv('SMTP_PORT')
        self.sender: str = os.getenv('EMAIL')
        self.password: str = os.getenv('PASSWORD')

    def mail(self, message: str, receiver: str):
        s = smtplib.SMTP(self.smtp_server, self.smtp_port)
        s.starttls()
        s.login(self.sender, self.password)
        s.sendmail(self.sender, receiver, message)
        s.quit()