from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "YOUR EMAIL"
TWITTER_PASSWORD = "YOUR PASSWORD"
TWITTER_LOGIN = "YOUR LOGIN"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(
            options=webdriver.ChromeOptions().add_experimental_option("detach", True)
        )
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)
        speed_test_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            value='a[aria-label="start speed test - connection type multi"]'
        )
        speed_test_btn.click()

        time.sleep(60)
        self.down = self.driver.find_element(
            By.CSS_SELECTOR,
            value='span[class="result-data-large number result-data-value download-speed"]'
        ).text
        self.up = self.driver.find_element(
            By.CSS_SELECTOR,
            value='span[class="result-data-large number result-data-value upload-speed"]'
        ).text

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")

        time.sleep(3)
        email_input = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'
        )
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)

        time.sleep(2)
        try:
            password_input = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
        )
        except:
            verify_input = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
            )
            verify_input.send_keys(TWITTER_LOGIN)
            verify_input.send_keys(Keys.ENTER)

            time.sleep(2)
            password_input = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
            )
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)
        else:
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)

        time.sleep(2)
        tweet_label = self.driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/span'
        )
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_label.send_keys(tweet)

        time.sleep(5)
        post_btn = self.driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button'
        )
        post_btn.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
