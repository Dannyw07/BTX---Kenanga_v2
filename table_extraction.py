from bs4 import BeautifulSoup

def extract_table_data(table1, table2):
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
    return combined_data,data1

# Example usage:
# Assuming you have already parsed the HTML content and obtained table1 and table2
# Replace table1 and table2 with your actual BeautifulSoup objects

# Example usage:
# combined_data = extract_table_data(table1, table2)
