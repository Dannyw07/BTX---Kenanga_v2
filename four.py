from libraries import *

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class four(tk.Frame):
    try:
        driver = webdriver.Chrome()
        #Initial URL
        driver.get('https://btx.kenanga.com.my/btxadmin/default.aspx')

        # Maximizing window
        driver.maximize_window()

        #Wait for the website to fully load
        time.sleep(2)

        # Make selenium to automate the login process (username,password,login button)
        username_input = driver.find_element(By.ID, 'ctl00_cntPlcHldrContent_txtUsrID')
        password_input = driver.find_element(By.ID, 'ctl00_cntPlcHldrContent_txtUsrPwd')
        submit_button = driver.find_element(By.ID,'ctl00_cntPlcHldrContent_ibSignIn')

        time.sleep(5)

        username_input.send_keys('ITHQOPR')
        password_input.send_keys('Kibb8888')
        submit_button.click()

        time.sleep(2)
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


        # In this page, it should be let user to choose the 'Day End Qnquiry' and 'Process Date'
        third_url = driver.current_url
        print("Third URL:", third_url)

        time.sleep(3)
        # Selecting the multi-select element by locating its id
        select = Select(driver.find_element(By.ID,"ctl00_cntPlcHldrContent_selEODEnquiry"))

        select.select_by_value("1,S")

        # Locate the datepicker input element
        datepicker_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_cntPlcHldrContent_txtDate")))
        # Get yesterday's date
        yesterday = datetime.datetime.now() - datetime.timedelta(days=3)
        yesterday_str = yesterday.strftime('%d/%m/%Y')  

        # Get today's date
        # today = datetime.datetime.now()
        # today_str = today.strftime('%d/%m/%Y')

        # Enter yesterday's date into the input field
        datepicker_input.clear()  # Clear any existing value
        datepicker_input.send_keys(yesterday_str)

        time.sleep(3)

        searchButton = driver.find_element(By.ID, "ctl00_cntPlcHldrContent_btnTpltUpdate_btnSearch")
        searchButton.click()

        forth_url = driver.current_url
        print("Forth URL:", forth_url)

        # Switch to the new window
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)

        # Maximize the window
        driver.maximize_window()

        fifth_url = driver.current_url
        print("Fifth URL:", fifth_url)

        time.sleep(2)

        nextButton = driver.find_element(By.ID, "lbNext")
        nextButton = driver.find_element(By.XPATH, "//table[@id='tblHeader']/tbody/tr/td/table/tbody/tr/td[8]/a[@id='lbNext']")
        nextButton.click()

        # Find the input field by its ID, for example
        # input_number_field = driver.find_element(By.ID,"txtSize")

        # # Clear the existing input value
        # input_number_field.clear()

        # # Type a new number into the input field
        # new_number = "100"  # Change this to the new number you want to input
        # input_number_field.send_keys(new_number)

        # # After setting the input value to 40
        # driver.execute_script("document.getElementById('txtSize').setAttribute('value', '100');")
        # # Disable the onkeypress event handler
        # driver.execute_script("document.getElementById('txtSize').removeAttribute('onkeypress');")

        # goButton = driver.find_element(By.ID, "ibGoto")
        # goButton.click()

        time.sleep(3)
        sixth_url = driver.current_url
        print("Sixth URL:", sixth_url)

        html_content_fifth_url = driver.page_source

        time.sleep(2)
        # Print the HTML content of the fifth URL
        # print("HTML Content of Fifth URL:", html_content_sixth_url)

        # Parse the HTML
        soup = BeautifulSoup(html_content_fifth_url, "html.parser")

        # Find the first table
        table1 = soup.find("table")

        # Find the second table with the id "gvEodEnqSumm"
        table2 = soup.find("table", id="gvEodEnqSumm")

        process_date_label = soup.find("span", id="Label1").text
        process_date_value = soup.find("span", id="lblProcDate").text

        # Print the extracted data
        print(process_date_label + ":", process_date_value)

        # Extract data from the BTX table
        data1, combined_data = extract_table_data(table1, table2)

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
        excel_file_path = os.path.join(subfolder_name, "tableFour.xlsx")

    # Create a new workbook and add a worksheet
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

        # Modify the HTML table to make the header grey
        soup = BeautifulSoup(html_table, "html.parser")
        tr_elements = soup.find_all("tr")[1:]  # Select rows starting from the third row

        for idx, element in enumerate(soup.find_all(["td"])):
            if element.name == "td":
                if element.text.strip() in ["Task ID", "Task Name", "Start Time", "Actual Start Time", "Actual End Time", "Duration", "Next Day", "Status"]:
                    element['style'] = 'background-color:#d7dae1; color:#0b14fe; font-weight:bold;'

        # Iterate over each table row, starting from the second row
        for tr_element in tr_elements[0:]:
            # Find all table cells within the current row
            td_elements = tr_element.find_all("td")
            
            # Iterate over each table cell within the current row
            for td_element in td_elements:
                # Add padding to the cell
                td_element['style'] = 'padding: 5px;'
            
            # Get the last table cell in the current row
            last_td_element = td_elements[-1]
            
            # Check if the text content of the last cell contains "Process Succeeded!"
            if "Process Succeeded!" in last_td_element.text.strip():
                # If it does, set the background color to green and text color to white
                last_td_element['style'] += 'background-color: green; color: white;'
            else:
                # If not, set the background color to red and text color to white
                last_td_element['style'] += 'background-color: red; color: white;'

        html_table = str(soup)
        # print(html_table)
        # Close the workbook

        def get_base64_encoded_image(image_path):
                with open(image_path, "rb") as img_file:
                    return base64.b64encode(img_file.read()).decode('utf-8')

        body = '''
            <p style="color: #a6a698; font-size:13px; font-family: Arial, sans-serif;">Regards,</p>
            <br>
            <p style="color: black; font-size: 14px; font-family: Calibri, sans-serif; font-weight: bold; margin: 0; padding:0;margin-bottom: 3px">IT OPERATIONS</p>
            <p style="color: #a6a698; font-size:13px; font-family: Arial, sans-serif; margin: 0; padding:0;margin-bottom: 3px">Group Digital, Technology & Transformation</p>
            <p style="color: #a6a698; font-size: 13px; font-family: Arial, sans-serif; font-weight: bold; margin: 0; padding:0;margin-bottom: 3px">Kenanga Investment Bank Berhad</p>
            <p style="color: #a6a698; font-size: 12px; font-family: Arial, sans-serif; margin: 0; padding:0;margin-bottom: 3px">Level 6, Kenanga Tower</p>
            <p style="color: #a6a698; font-size: 12px; font-family: Arial, sans-serif;margin: 0; padding:0;margin-bottom: 4px">237, Jalan Tun Razak, 50400 Kuala Lumpur</p>
            <p style="color: #4472c4; font-size: 11px; font-family: Arial, sans-serif;margin: 0; padding:0;margin-bottom: 3px">Tel: GL +60 3 21722888 (Ext:8364 / 8365 / 8366 / 8357) </p>
            <br>
            <img src="data:image/png;base64, {}" alt="image1"> <!-- Embed image1 -->
            <br>
            <img src="data:image/png;base64, {}" alt="image2" > <!-- Embed image2 -->
            '''.format(get_base64_encoded_image(resource_path('images/image1.png')), get_base64_encoded_image(resource_path('images/image2.png')))
        
        html_content = f"<p>Process Date: {process_date_value}</p>\n\n{html_table}\n{body}"
        # Set up the email details
        sender_email = "dannywong@kenanga.com.my"
        # receiver_email = ["dannywong@kenanga.com.my"]
        receiver_email = ["dannywong@kenanga.com.my"]
        # cc_emails = ["itklm@kenanga.com.my"]

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] =  ','.join(receiver_email)
        # message['Cc'] = ','.join(cc_emails)
        message["Subject"] = f"[Testing Email] BTX Start Of Day process monitoring {process_date_value} - checking @ 7.00am "

        # Add HTML table to the email body
        message.attach(MIMEText(html_content, "html"))

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
        time.sleep(2)
        print("Logout successful")

        # Close the main window
        driver.close()
    except NoSuchWindowException:
        print("The browser window was unexpectedly closed.")
    # You might want to take appropriate action here, such as reopening the browser.
    finally:
        # Make sure to quit the WebDriver to release resources
        driver.quit()

    
