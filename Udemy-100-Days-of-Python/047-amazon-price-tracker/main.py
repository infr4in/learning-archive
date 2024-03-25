import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7"
}  # we use the header to return the actual html of the page

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(name="span", class_="aok-offscreen").getText()
price_val = float(price.split("$")[1])
title = soup.find(name="span", id="productTitle").get_text().strip()
BUY_PRICE = 100

if price_val < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
