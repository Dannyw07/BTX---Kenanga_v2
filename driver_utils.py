# driver_utils.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def initialize_driver():
    # Define Chrome options
    chrome_options = Options()
    # Add option to clear cache
    chrome_options.add_argument("--disable-application-cache")
    # Create a new instance of Chrome WebDriver with the defined options
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
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

