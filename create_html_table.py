from bs4 import BeautifulSoup

def modify_html_table(html_table):
    # Modify the HTML table to make the header grey
    soup = BeautifulSoup(html_table, "html.parser")
    tr_elements = soup.find_all("tr")[1:]  # Select rows starting from the second row

    # Iterate over each table cell in the header row
    for idx, element in enumerate(soup.find_all(["td"])):
        if element.name == "td":
            # Check if the text content matches specific headers
            if element.text.strip() in ["Task ID", "Task Name", "Start Time", "Actual Start Time", "Actual End Time", "Duration", "Next Day", "Status"]:
                # Apply styling for the header cells
                element['style'] = 'background-color:#d7dae1; color:#0b14fe; font-weight:bold;'

    # Iterate over each table row, starting from the second row
    for tr_element in tr_elements:
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
        elif "Process started" in last_td_element.text.strip():
            # If it contains "Process started", set the background color to yellow and text color to black
            last_td_element['style'] += 'background-color: yellow; color: white;'
        else:
            # If not, set the background color to red and text color to white
            last_td_element['style'] += 'background-color: red; color: white;'

    # Convert the modified HTML table back to string
    modified_html_table = str(soup)
    
    return modified_html_table

# Example usage:
# html_table = "<table>...</table>"  # Replace ... with your actual HTML table content
# modified_table = modify_html_table(html_table)
# print(modified_table)
