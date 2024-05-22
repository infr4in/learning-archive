from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

PHONE_NUMBER = "01781626443"
PASSWORD = "19724856Dw"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")

# Reject cookies
time.sleep(3)
tinder_cookies = driver.find_element(
    By.XPATH,
    value='//*[@id="t425926696"]/div/div[2]/div/div/div[1]/div[2]/button'
)
tinder_cookies.click()

# Click Log in button
time.sleep(3)
login_btn = driver.find_element(
    By.XPATH,
    value='//*[@id="t425926696"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
)
login_btn.click()

# Log in with facebook
time.sleep(3)
facebook_login = driver.find_element(
    By.XPATH,
    value='//*[@id="t-1302454380"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button'
)
facebook_login.click()

# Switch to Facebook window
time.sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# Reject facebook cookies
time.sleep(3)
facebook_cookies = driver.find_element(
    By.CSS_SELECTOR,
    value='button[data-testid="cookie-policy-manage-dialog-decline-button"]'
)
facebook_cookies.click()

# Feel inputs & log in
time.sleep(3)
input_phone = driver.find_element(By.CSS_SELECTOR, value='input[id="email"]')
input_phone.send_keys(PHONE_NUMBER)
input_password = driver.find_element(By.CSS_SELECTOR, value='input[id="pass"]')
input_password.send_keys(PASSWORD)
input_password.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)

# Allow for location
time.sleep(10)
allow_location_btn = driver.find_element(
    By.XPATH,
    value='//*[@id="t-1302454380"]/main/div/div/div/div[3]/button[1]'
)
allow_location_btn.click()

# Not interested for notifications
time.sleep(3)
not_interested_btn = driver.find_element(
    By.XPATH,
    value='//*[@id="t-1302454380"]/main/div/div/div/div[3]/button[2]'
)
not_interested_btn.click()

# Click free 100 "Likes" per day
time.sleep(3)
for n in range(20):
    # Add 1 sec delay between likes
    time.sleep(1)

    try:
        like_btn = driver.find_element(
            By.CSS_SELECTOR,
            value='div[class="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc($c-ds-border-gamepad-like-default)"] '
                  'button[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgi($g-ds-background-like):a"]'
        )
        like_btn.click()

    # Catches pop-up
    except ElementClickInterceptedException:
        try:
            popup = driver.find_element(
                By.XPATH,
                value='//*[@id="t-1302454380"]/main/div/div[2]/button[2]'
            )
            popup.click()

        # When "Like" btn has not yet loaded, then just wait 2 sec.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
