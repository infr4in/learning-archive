from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

SIMILAR_ACC = "YOUR TARGET ACC"
USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASS"


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(2)

        cookies = self.driver.find_element(
            By.XPATH,
            value="//button[contains(text(), 'Отклонить необязательные файлы cookie')]"
        )
        cookies.click()

        username_input = self.driver.find_element(
            By.CSS_SELECTOR,
            value='input[name="username"]'
        )
        password_input = self.driver.find_element(
            By.CSS_SELECTOR,
            value='input[name="password"]'
        )

        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)

        password_input.send_keys(Keys.ENTER)

        time.sleep(5)
        save_popup = self.driver.find_element(
            By.XPATH,
            value="//div[contains(text(), 'Не сейчас')]"
        )
        save_popup.click()

        time.sleep(2)
        notifications_popup = self.driver.find_element(
            By.XPATH,
            value="//button[contains(text(), 'Не сейчас')]"
        )
        notifications_popup.click()

    def follow(self):
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACC}")

        time.sleep(5)
        followers_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            value=f'a[href="/{SIMILAR_ACC}/followers/"]'
        )
        followers_btn.click()

        time.sleep(2)
        all_followers_page = self.driver.find_element(
            By.XPATH,
            value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'
        )
        for _ in range(5):
            follow_buttons = self.driver.find_elements(
                By.CSS_SELECTOR,
                value='button[class=" _acan _acap _acas _aj1- _ap30"]'
            )

            for follow_button in follow_buttons:
                try:
                    follow_button.click()
                    time.sleep(1)
                except (ElementClickInterceptedException, NoSuchElementException) as e:
                    pass

                try:
                    popup_btn = self.driver.find_element(
                        By.CSS_SELECTOR,
                        value='button[class="_a9-- _ap36 _a9_1"]'
                    )
                    popup_btn.click()
                    time.sleep(1)
                except (ElementClickInterceptedException, NoSuchElementException) as e:
                    pass

            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", all_followers_page)
            time.sleep(2)


bot = InstaFollower()
bot.login()
bot.follow()
