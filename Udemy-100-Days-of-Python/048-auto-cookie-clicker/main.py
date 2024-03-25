from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

# Get all upgrade ids
upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store div")
upgrade_ids = [upgrade.get_attribute("id") for upgrade in upgrades]

# Breakpoints
timeout = time.time() + 5  # 5 seconds
five_min = time.time() + 60*5  # 5 minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags (because there's a price value)
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")

        # Convert <b> text into an integer price
        upgrade_prices = []  # [15, 100, 500, ... ]
        for price in all_prices:
            if price.text != "":
                cost = int(price.text.split("-")[1].strip().replace(",", ""))
                upgrade_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}  # {15: 'buyCursor', 100: 'buyGrandma', ... }
        for n in range(len(upgrade_prices)):
            cookie_upgrades[upgrade_prices[n]] = upgrade_ids[n]

        # Get current cookie count
        money = driver.find_element(By.XPATH, value='//*[@id="money"]').text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        # Find upgrades that we can currently buy
        available_upgrades = {}   # {15: 'buyCursor', 100: 'buyGrandma', ... }
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                available_upgrades[cost] = id

        # Find the most expensive available upgrade
        highest_price_available_upgrade = max(available_upgrades)
        to_purchase_id = available_upgrades[highest_price_available_upgrade]

        # Buys the most expensive upgrade
        driver.find_element(By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.XPATH, value='//*[@id="cps"]').text
        print(cookie_per_s)
        break
