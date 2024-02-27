import smtplib
from twilio.rest import Client

TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
FROM_NUMBER = "YOUR TWILIO VIRTUAL NUMBER"
TO_NUMBER = "YOUR TO NUMBER"
MAIL_SMTP = "smtp.gmail.com"
MY_EMAIL = "YOUT EMAIL"
MY_PASSWORD = "YOUR PASSWORD"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=FROM_NUMBER,
            to=TO_NUMBER,
        )

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_SMTP) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
