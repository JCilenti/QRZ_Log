# Open a log file and save contents
# access QRZ and pull info
import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.qrz.com/db/')
id_box = driver.find_element('xpath', '//*[@id="cs"]')
#id_box = driver.find_element("name", "query")
id_box.send_keys('KO4KRC')
time.sleep(5)
search = driver.find_element('xpath', '//*[@id="qform"]/table/tbody/tr[1]/td[2]/input')
search.click()
