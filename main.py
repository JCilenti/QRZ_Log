# Open a log file and save contents
# access QRZ and pull info
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date
import sys
import csv

requested_call_sign = input("Please enter a call sign: ")
username = input("Please enter your username: ")
password = input("Please enter your password: ")

divider = "*" * 50

# need to check if file exists
# Prompt user for email and password

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

today = date.today()
d = today.strftime("%B %d, %Y")

driver = webdriver.Chrome()
driver.get('https://www.qrz.com/login')
user_id_box = driver.find_element('xpath', '//*[@id="username"]')
user_id_box.send_keys(username)
next_button = driver.find_element('xpath', '//*[@id="login-form"]/div/div[2]/div[3]/div/div[2]/button')
next_button.click()
time.sleep(3) # was 8
pswd_box = driver.find_element('xpath', '//*[@id="password"]')
pswd_box.send_keys(password)
sign_in_button = driver.find_element('xpath', '//*[@id="login-form"]/div/div[2]/div[4]/div/div[2]/button')
sign_in_button.click()
time.sleep(10) # was 10
call_sign_search = driver.find_element('xpath', '//*[@id="tquery"]')
call_sign_search.send_keys(requested_call_sign) # this needs to be an argument passed by the user
cs_search_button = driver.find_element('xpath', '//*[@id="tsubmit"]')
cs_search_button.click()
time.sleep(5)
detail_button = driver.find_element('xpath', '//*[@id="ui-id-2"]')
detail_button.click()
time.sleep(5)

# Name and address
user_data_main = driver.find_element(By.CLASS_NAME, 'm0')
user_text = user_data_main.text

# License type
user_data_class = driver.find_element(By.XPATH, '//*[@id="dt"]/tbody/tr[4]/td[2]')
class_text = user_data_class.text

# Grid location
user_data_grid = driver.find_element(By.XPATH, '//*[@id="dt"]/tbody/tr[7]/td[2]')
grid_text = user_data_grid.text

# Map of current location
show_map = driver.find_element(By.XPATH, '//*[@id="dbmap"]/input')
#new_text = user_text.strip('\n')

only_name = user_text.splitlines()[0]
only_address = user_text.splitlines()[1] + '\n' + user_text.splitlines()[2]
print(divider)
print("Name: ", only_name)
print(divider)
print("Address: ", only_address)
print(divider)
print("Class: ", class_text)
print(divider)
print("Grid: ", grid_text)
print(divider)
print("Time: ", current_time)
print("Date: ", d)
print(divider)

show_map.click()
time.sleep(5)
'''
with open('map.png', 'wb') as file:
    m = driver.find_element(By.XPATH, '//*[@id="dbmap"]')
    file.write(m.screenshot_as_png)

n = len(sys.argv)
print("Total arguments passed:", n)
print("\nName of Python script:", sys.argv[0])
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
'''



log_file = open('qrz_log.xlsx', 'a')
log_file = csv.writer(log_file)
# Only print the title line once (fix this)
log_file.writerow(['Log #', 'Time', 'Date', 'Name', 'Call Sign', 'Address', 'Class', 'Grid'])
log_file.writerow(['1', current_time, d, only_name, requested_call_sign, only_address, class_text, grid_text])
print('[WRITING TO FILE...]')
print('All Records Imported Successfully !')
driver.quit()