# Import Libraries
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date
import sys
import csv

def main():

    log_counter = 1

    requested_call_sign = input("Please enter a call sign: ")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    divider = "*" * 50

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
    user_data_grid = driver.find_element(By.XPATH, '//*[@id="dt"]/tbody/tr[9]/td[2]')
    grid_text = user_data_grid.text

    # Map of current location
    show_map = driver.find_element(By.XPATH, '//*[@id="dbmap"]/input')

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

    def check_for_top_row():
        #log_file = open('qrz_log.xlsx', 'x')
        file_obj = open('qrz_log.xlsx', 'r')
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            if row[0] == 'Log #':
                continue
            else:
                file_obj = open('qrz_log.xlsx', 'w')
                writer_obj = csv.writer(file_obj)
                log_file_w.writerow(['Log #', 'Time', 'Date', 'Name', 'Call Sign', 'Address', 'Class', 'Grid'])

    check_for_top_row()
    log_file = open('qrz_log.xlsx', 'a')
    log_file_w = csv.writer(log_file)
    log_file_w.writerow([str(log_counter), current_time, d, only_name, requested_call_sign, only_address, class_text, grid_text])
    print('[WRITING TO FILE...]')
    print('All Records Imported Successfully !')
    print("Log Number: " + str(log_counter))
    driver.quit()
    log_counter = log_counter + 1

if __name__ == '__main__':
    main()


