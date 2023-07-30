# Open a log file and save contents
# access QRZ and pull info
import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.qrz.com/login')
user_id_box = driver.find_element('xpath', '//*[@id="username"]')
user_id_box.send_keys('jecilenti@gmail.com')
next_button = driver.find_element('xpath', '//*[@id="login-form"]/div/div[2]/div[3]/div/div[2]/button')
next_button.click()
time.sleep(8)
pswd_box = driver.find_element('xpath', '//*[@id="password"]')
pswd_box.send_keys('WestPoint1322')
sign_in_button = driver.find_element('xpath', '//*[@id="login-form"]/div/div[2]/div[4]/div/div[2]/button')
sign_in_button.click()
time.sleep(10)

