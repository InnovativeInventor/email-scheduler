import smtplib
import validators
import config
from email.message import EmailMessage

class Email:
    def __init__(self):
        self.smtp = smtplib.SMTP_SSL('email-smtp.us-east-1.amazonaws.com', port=465)
        self.smtp.login(config.EMAIL_USERNAME, config.EMAIL_PASSWORD)

    def send(self, recipient: str, subject = "", msg = ""):
        """
        Sends a message
        """
        email = EmailMessage()
        if validators.email(recipient) and subject and msg:
            email['Subject'] = subject.rstrip()
            email['From'] = "notify@cpu.party"
            email['To'] = recipient.rstrip()
            email['BCC'] = "root@max.fan"
            email.set_content(msg.rstrip())

            self.smtp.send_message(email)

