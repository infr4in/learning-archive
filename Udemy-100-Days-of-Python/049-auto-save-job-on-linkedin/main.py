from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "YOUR EMAIL"
ACCOUNT_PASSWORD = "YOUR PASSWORD"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)

# Click Reject Cookies Button
time.sleep(3)
reject_button = driver.find_element(by=By.XPATH, value='//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[2]')
reject_button.click()

# Click Sign in Button
time.sleep(3)
sign_in_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
sign_in_button.click()

# Sign in
time.sleep(3)
email_field = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# Hide Message Box
time.sleep(3)
msg_button = driver.find_element(by=By.XPATH, value='//*[@id="ember112"]')
msg_button.click()

# Get all Jobs
time.sleep(3)
all_jobs = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container__link")

# Save all Jobs
for job in all_jobs:
    # Go to Job
    job.click()
    time.sleep(3)
    try:
        # Click Save Button
        save_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
        save_button.click()
    except NoSuchElementException:
        continue
