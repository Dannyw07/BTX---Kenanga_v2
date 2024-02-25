# driver_utils.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def navigate_to_initial_url(driver, initial_url):
    driver.get(initial_url)
    time.sleep(2)  # Wait for the website to fully load

def login(driver, username, password):
    username_input = driver.find_element(By.ID, 'ctl00_cntPlcHldrContent_txtUsrID')
    password_input = driver.find_element(By.ID, 'ctl00_cntPlcHldrContent_txtUsrPwd')
    submit_button = driver.find_element(By.ID, 'ctl00_cntPlcHldrContent_ibSignIn')

    time.sleep(5)

    username_input.send_keys(username)
    password_input.send_keys(password)
    submit_button.click()

    time.sleep(5)
    # You might want to add some waits here as well
