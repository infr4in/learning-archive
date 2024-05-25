import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM_URL = "YOUR GOOGLE FORM ULR"

response = requests.get(ZILLOW_CLONE_URL)
soup = BeautifulSoup(response.text, "html.parser")

all_links_html = soup.select('.StyledPropertyCardDataArea-anchor')
all_links = [link.get("href") for link in all_links_html]

# get all text prices from span element
# and then sort them using .join method
all_prices_html = soup.select('span[data-test="property-card-price"]')
price_regex = "$,0123456789"
all_prices = [''.join(char for char in price.getText() if char in price_regex) for price in all_prices_html]

all_addresses_html = soup.select('address[data-test="property-card-addr"]')
all_addresses = [address.getText().strip() for address in all_addresses_html]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for i in range(len(all_links)):
    driver.get(GOOGLE_FORM_URL)
    time.sleep(2)

    address_input = driver.find_element(
        By.CSS_SELECTOR,
        value='[aria-labelledby="i1"]'
    )
    price_input = driver.find_element(
        By.CSS_SELECTOR,
        value='[aria-labelledby="i5"]'
    )
    link_input = driver.find_element(
        By.CSS_SELECTOR,
        value='[aria-labelledby="i9"]'
    )
    submit_btn = driver.find_element(
        By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
    )

    address_input.send_keys(all_addresses[i])
    price_input.send_keys(all_prices[i])
    link_input.send_keys(all_links[i])
    submit_btn.click()
