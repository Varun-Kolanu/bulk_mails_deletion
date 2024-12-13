import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv()

mail = os.getenv("EMAIL_ID")
passwd = os.getenv("EMAIL_PASSWORD")

options = uc.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = uc.Chrome(options=options)

driver.get('https://mail.google.com')

email = driver.find_element(By.ID, 'identifierId')
email.send_keys(mail)
email.send_keys(Keys.ENTER)
time.sleep(8)  # Waiting for page to load

password = driver.find_element(By.NAME, 'Passwd')
password.send_keys(passwd)
password.send_keys(Keys.ENTER)
time.sleep(10)

select_all_checkbox = driver.find_element(By.XPATH, '//span[@role="checkbox"]')
delete_button = driver.find_element(By.XPATH, '//*[@aria-label="Delete"]/div')

for i in range(50):

    select_all_checkbox.click()
    time.sleep(5)

    delete_button.click()
    time.sleep(5)

    print(f"{100*(i+1)} emails Deleted")

driver.quit()
