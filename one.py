import tkinter as tk
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import os
from socket import timeout as SocketTimeoutError
import time
import datetime
from dotenv import load_dotenv
load_dotenv()
from selenium.webdriver.support.ui import Select
import datetime
from selenium.common.exceptions import NoSuchWindowException
from driver_utils import initialize_driver, navigate_to_initial_url, login
from emailBody import generate_email_body, image1_base64, image2_base64
from create_excel import generate_excel_file
from create_html_table import modify_html_table
from socket import timeout as SocketTimeoutError
from selenium.webdriver.support import expected_conditions as EC
# import logging
# Set up logging configuration
# logging.basicConfig(filename='one.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class one(tk.Frame):
    
    try: 
        current_directory = os.path.dirname(os.path.abspath(__file__))
        env_file_path = os.path.join(current_directory,'.env')
        print("Path to .env file", env_file_path)
        # logging.info("Path to .env file: %s", env_file_path)

        # Maximum number of retries
        max_retries = 3
        retry_count = 0

        # Initialize WebDriver
        driver = initialize_driver()

        # Navigate to initial URL
        initial_url = 'https://btx.kenanga.com.my/btxadmin/default.aspx'
        navigate_to_initial_url(driver, initial_url)

        # Perform login
        # username = 'ITHQOPR'
        # password = 'Kibb8888'
        username = os.getenv('USER_NAME')
        password = os.getenv('PASSWORD')
        print(f"username: {username}")
        print(f"password: {password}")
        # logging.info("Username: %s", username)
        # logging.info("Password: %s", password)
        login(driver, username, password)

        # Click on the image button to navigate to another page
        # The button image name is 'Day End Maintenance'

        # Define Day EndM XPaths
        day_end_m_xpaths =[
            "//img[@src='/btxadmin/images/demo/icons/i_dayEndM_off.jpg']",
            "//img[@src='/btxadmin/images/demo/icons/i_dayEndM_on.jpg']"
        ]

        # Iterate through each XPath
        for xpath in day_end_m_xpaths:
            try:
                # Try to find the element
                dayEndM_image = driver.find_element(By.XPATH,xpath)
                # If found, click on it
                dayEndM_image.click()
                # Exit loop if element is found and clicked
                break 
            except NoSuchElementException:
                # If element is not found, continue to the next XPath
                continue

        # In here, after navigating to the new page, get the new url again
        # In this page, it should be let user to choose the 'Day End Enquiry'

        time.sleep(4)
        
        second_url = driver.current_url
        print("Second URL:", second_url)
        # logging.info("Second URL: %s", second_url)

        # Define Day End Enquiry XPaths
        day_end_enquiry_xpaths = [
            "//img[@src='/btxadmin/images/demo/icons/i_dayEndE_on.jpg']",
            "//img[@src='/btxadmin/images/demo/icons/i_dayEndE_off.jpg']"
        ]

        # Iterate through each XPath
        for xpath in day_end_enquiry_xpaths:
            try:
                # Try to find the element
                dayEndEnquiry_image = driver.find_element(By.XPATH,xpath)
                # If found, click on it
                dayEndEnquiry_image.click()
                # Exit loop if element is found and clicked
                break 
            except NoSuchElementException:
                # If element is not found, continue to the next XPath
                continue

        # In this page, it should be let user to choose the 'Day End Enquiry' and 'Process Date'
        third_url = driver.current_url
        print("Third URL:", third_url)
        # logging.info("Third URL: %s", third_url)

        # Wait for the multi-select element to be present
        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID,'ctl00_cntPlcHldrContent_selEODEnquiry'))
        )
        # Once the multi-select element is present, create the Select object
        select = Select(select_element)
        
        # Select an option from the dropdown (change index as needed)
        select.select_by_value("1,S")

        # Locate the datepicker input element
        datepicker_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_cntPlcHldrContent_txtDate"))
        )

        # Get yesterday's date
        # yesterday = datetime.datetime.now() - datetime.timedelta(days=4)
        # yesterday_str = yesterday.strftime('%d/%m/%Y')  

        # # Get today's date
        today = datetime.datetime.now()
        today_str = today.strftime('%d/%m/%Y')

        # Enter today's date into the input field
        datepicker_input.clear()  # Clear any existing value
        datepicker_input.send_keys(today_str)

        while retry_count < max_retries:
            try:
                # Wait for the search button element to be present
                searchButton = WebDriverWait(driver,10).until(
                    EC.presence_of_element_located((By.ID,'ctl00_cntPlcHldrContent_btnTpltUpdate_btnSearch'))
                )
                searchButton.click()
                break # Exit the loop if successfully clicked
            except TimeoutException:
                print(f"Error: search button not found within 10 seconds (Retry {retry_count + 1}/{max_retries})")
                # logging.error("Error: Search button not found within 10 seconds (Retry %d/%d): %s", retry_count + 1, max_retries)
                retry_count += 1
                # Wait for 2 seconds before retrying again
                time.sleep(2)
        else:
            print(f"Error: Failed to find search button after {max_retries} retries")
            # logging.error(f"Error: Failed to find search button after {max_retries} retries")
            # Add additional error handling or raise an exception as needed

        forth_url = driver.current_url
        print("Forth URL:", forth_url)
        # logging.info("Forth URL: %s", forth_url)

        # Switch to the new window
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)

        # Maximize the new window
        driver.maximize_window()

        fifth_url = driver.current_url
        print("Fifth URL:", fifth_url)
        # logging.info("Fifth URL: %s", fifth_url)

        driver.get(fifth_url)

        # Get the HTML content of the fifth URL
        html_content_fifth_url = driver.page_source

        # Parse the HTML
        soup = BeautifulSoup(html_content_fifth_url, "html.parser")

        # Find the first table
        table1 = soup.find("table")

        # Find the second table with the id "gvEodEnqSumm"
        table2 = soup.find("table", id="gvEodEnqSumm")

        process_date_label = soup.find("span", id="Label1").text
        process_date_value = soup.find("span", id="lblProcDate").text

        # Print the extracted date
        print(process_date_label + ":", process_date_value)
        # logging.info("%s: %s", process_date_label, process_date_value)

        # Extract data from the first table
        data1 = []
        for row in table1.find_all("td", id="tdBG"):
            row_data = []
            for cell in row.find_all(["span"]):
                cell_text = cell.get_text(strip=True)
                if cell_text:  # Check if cell text is not empty
                    row_data.append(cell_text)
            if row_data:  # Only append if row_data is not empty
                data1.append(row_data)

        # Extract table headers from the second table
        table2_headers = []
        for th in table2.find_all("th"):
            header_text = th.get_text(strip=True)
            if header_text:  # Check if header text is not empty
                table2_headers.append(header_text)

        # Extract data from the second table
        data2 = []
        for row in table2.find_all("tr"):
            row_data = []
            # Flag to check if any non-empty cell is found in the row
            non_empty_found = False
            for cell in row.find_all("td"):
                cell_text = cell.get_text(strip=True)
                if cell_text: # If cell text is not empty
                    non_empty_found = True
                row_data.append(cell_text)
            # Append the row data only if at least one non-empty cell is found
            if non_empty_found:
                data2.append(row_data)

        # Combine data from table1 and table2
        combined_data = data1 + [table2_headers] + data2

        # Create a folder named "xlsx_files" if it doesn't exist
        folder_name = "xlsx_files"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Get current date
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')

        # Create a new folder with the current date inside the 'xlsx_files'
        subfolder_name = os.path.join(folder_name, current_date)
        if not os.path.exists(subfolder_name):
            os.makedirs(subfolder_name)

        # Path to the Excel file inside the subfolder
        excel_file_path = os.path.join(subfolder_name, "tableOne.xlsx")

        generate_excel_file(excel_file_path, combined_data, data1)

        # Load the Excel file
        file_path = excel_file_path
        try:
            df = pd.read_excel(file_path,header=None)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            exit()
        
        df = df.fillna('')

        # Convert the DataFrame to an HTML table with no index
        html_table = df.to_html(index=False, header=False)

        modified_html_table = modify_html_table(html_table)

        body = generate_email_body(image1_base64,image2_base64)

        html_content = f"<p><strong>Process Date : </strong>{process_date_value}</p>\n\n{modified_html_table}<p><strong>BTX web portal login ID used : </strong>{username}</p>\n{body}"

        # Load environment variables from .env file
        smtp_server_ip = os.getenv('SMTP_SERVER_IP')
        smtp_port = os.getenv('SMTP_PORT')
        smtp_username = os.getenv('EMAIL_ADDRESS')
        recipient_email = os.getenv('RECIPIENT_ADDRESS')
        cc_email = os.getenv('CC_ADDRESS')

        print(f'smtp_server_ip: {smtp_server_ip}')
        print(f'smtp_port: {smtp_port}')
        print(f'smtp_username: {smtp_username}')
        # logging.info("SMTP Server IP: %s", smtp_server_ip)
        # logging.info("SMTP Port: %s", smtp_port)
        # logging.info("SMTP Username: %s", smtp_username)

        if ',' in recipient_email:
            # Split string into a list of email addresses
            recipient_emails = recipient_email.split(',')
        else:
            # Treat it as a single email address
            recipient_emails = [recipient_email]
        print(f'recipient_email: {recipient_emails}')
        # logging.info("Recipient Email: %s", recipient_emails)

        if ',' in cc_email:
            # Split string into a list of email addresses
            cc_emails = cc_email.split(',')
        else:
            # Treat it as a single email address
            cc_emails = [cc_email]
        print(f'cc_email: {cc_emails}')
        # logging.info("CC Email: %s", cc_emails)

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = smtp_username
        message["To"] =  ','.join(recipient_emails)
        message['Cc'] = ','.join(cc_emails)
        message["Subject"] = f"BTX Start Of Day process monitoring {process_date_value} - checking @ 4.30am "

        # Add HTML table to the email body
        message.attach(MIMEText(html_content, "html"))

        # Set the timeout value in seconds
        timeout = 10  # Adjust this value as needed

        try:
            with smtplib.SMTP(timeout=timeout) as server:
                server.connect(smtp_server_ip, smtp_port)
                # Combine both recipient_emails and cc_emails into a single list
                all_recipients = recipient_emails + cc_emails
                server.sendmail(smtp_username, all_recipients, message.as_string())
                print("Success", f"Email successfully sent using {smtp_server_ip}!")
                # logging.info("Email successfully sent using %s!", smtp_server_ip)
        except SocketTimeoutError as e:
            print(f"TimeoutError occurred while connecting to SMTP server: {e}")
            # logging.error("TimeoutError occurred while connecting to SMTP server: %s", e)
            # Additional handling for the timeout error, such as retrying the operation or logging the error.
        except smtplib.SMTPException as e:
            print("Error", f"SMTPException occurred: {e}")
            # logging.error("SMTPException occurred: %s", e)
            # Additional handling for SMTP exceptions, such as retrying the operation or logging the error.
        except Exception as e:
            print("Error", f"An unexpected error occurred: {e}")
            # logging.error("An unexpected error occurred: %s", e)
            # Additional handling for any other unexpected exceptions, such as logging the error.

        time.sleep(2)
        # Close the new window
        driver.close()

        # Switch back to the main window
        driver.switch_to.window(driver.window_handles[0])
        # time.sleep(3)

        #Perform Logout Operation
        while retry_count < max_retries:
            try:
                # Wait for the logout button to be clickable
                logoutButton = WebDriverWait(driver,10).until(
                    EC.presence_of_element_located((By.ID,'ctl00_lbtnLogout'))
                )
                # Once the button is clickable, click it
                logoutButton.click()
                break # Exit the loop if successfully clicked
            except TimeoutException:
                # Handle the case where logout button is not found within 10 seconds
                print(f'Error: Logout button not found within 10 seconds (Retry {retry_count + 1}/{max_retries})')
                # logging.error("Logout button not found within 10 seconds (Retry %d/%d)", retry_count + 1, max_retries)
                retry_count +=1
                # Wait for 2 seconds before retrying again
                time.sleep(2)
        else:
            print(f"Error: Failed to find logout button after {max_retries} retries")
            # logging.error("Failed to find logout button after %d retries", max_retries)
            # Add additional error handling or raise an exception as needed      

        # Add a delay to ensure the logout process completes
        time.sleep(5)
        print("Logout successful")
        # logging.info("Logout successful")

        # Close the main window
        driver.close()
    except NoSuchWindowException:
        print("The browser window was unexpectedly closed.")
        # logging.error("The browser window was unexpectedly closed.")
    # You might want to take appropriate action here, such as reopening the browser.
    finally:
        # Make sure to quit the WebDriver to release resources
        driver.quit()


   
    
