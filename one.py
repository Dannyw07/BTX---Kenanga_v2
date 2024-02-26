from libraries import *

class one(tk.Frame):
    
    try: 
        # Initialize WebDriver
        driver = initialize_driver()

        # Navigate to initial URL
        initial_url = 'https://btx.kenanga.com.my/btxadmin/default.aspx'
        navigate_to_initial_url(driver, initial_url)

        # Perform login
        username = 'ITHQOPR'
        password = 'Kibb8888'
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

        time.sleep(3)
        # Selecting the multi-select element by locating its id
        select = Select(driver.find_element(By.ID,"ctl00_cntPlcHldrContent_selEODEnquiry"))

        # Select an option from the dropdown (change index as needed)
        select.select_by_value("1,S")

        # Locate the datepicker input element
        datepicker_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_cntPlcHldrContent_txtDate")))
        # Get yesterday's date
        # yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        # yesterday_str = yesterday.strftime('%d/%m/%Y')  

        # Get today's date
        today = datetime.datetime.now()
        today_str = today.strftime('%d/%m/%Y')

        # Enter yesterday's date into the input field
        datepicker_input.clear()  # Clear any existing value
        datepicker_input.send_keys(today_str)

        time.sleep(3)

        searchButton = driver.find_element(By.ID, "ctl00_cntPlcHldrContent_btnTpltUpdate_btnSearch")
        searchButton.click()

        forth_url = driver.current_url
        print("Forth URL:", forth_url)

        # Switch to the new window
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)

        # Maximize the new window
        driver.maximize_window()

        fifth_url = driver.current_url
        print("Fifth URL:", fifth_url)

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
            for cell in row.find_all(["td"]):
                cell_text = cell.get_text(strip=True)
                if cell_text:  # Check if cell text is not empty
                    row_data.append(cell_text)
            if row_data:  # Only append if row_data is not empty
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

        html_content = f"<p>Process Date: {process_date_value}</p>\n\n{modified_html_table}\n{body}"

        # Set up the email details
        sender_email = "dannywong@kenanga.com.my"
        receiver_email = ["dannywong@kenanga.com.my"]
        # cc_emails = ["itklm@kenanga.com.my"]

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] =  ','.join(receiver_email)
        # message['Cc'] = ','.join(cc_emails)
        message["Subject"] = f"[Testing Email] BTX Start Of Day process monitoring {process_date_value} - checking @ 4.30am "

        # Add HTML table to the email body
        message.attach(MIMEText(html_content, "html"))

        # Set the timeout value in seconds
        timeout = 10  # Adjust this value as needed

        try:
            with smtplib.SMTP(timeout=timeout) as server:
                server.connect("172.21.5.60", 25)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print("Success", "Email successfully sent!")
        except SocketTimeoutError as e:
            print(f"TimeoutError occurred while connecting to SMTP server: {e}")
            # Additional handling for the timeout error, such as retrying the operation or logging the error.
        except smtplib.SMTPException as e:
            print("Error", f"SMTPException occurred: {e}")
            # Additional handling for SMTP exceptions, such as retrying the operation or logging the error.
        except Exception as e:
            print("Error", f"An unexpected error occurred: {e}")
            # Additional handling for any other unexpected exceptions, such as logging the error.

        time.sleep(2)
        # Close the new window
        driver.close()

        # Switch back to the main window
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)
        #Perform Logout Operation
        logoutButton = driver.find_element(By.ID, "ctl00_lbtnLogout")
        # logoutButton = driver.find_element(By.XPATH, "//table[@id='tblHeader']/tbody/tr/td/table/tbody/tr/td[8]/a[@id='lbNext']")
        logoutButton.click()
        # Add a delay to ensure the logout process completes
        time.sleep(5)
        print("Logout successful")

        # Close the main window
        driver.close()
    except NoSuchWindowException:
        print("The browser window was unexpectedly closed.")
    # You might want to take appropriate action here, such as reopening the browser.
    finally:
        # Make sure to quit the WebDriver to release resources
        driver.quit()


   
    
