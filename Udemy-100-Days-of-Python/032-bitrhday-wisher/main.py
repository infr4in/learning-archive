# Change MY_EMAIL, MY PASSWORD, birthdays.csv,
# letters in ./letter_templater/
# and check smtplib.SMTP("smtp.gmail.com")

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "your_mail@gmail.com"
MY_PASSWORD = "your pass from mail"

today = {
    "month": datetime.now().month,
    "day": datetime.now().day
}

data = pandas.read_csv("./birthdays.csv")
birthdays = data.to_dict(orient="records")

for birthday in birthdays:
    if birthday["month"] == today["month"] and birthday["day"] == today["day"]:
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
            letter = letter_file.read()
            letter = letter.replace("[NAME]", birthday["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter}"
            )
