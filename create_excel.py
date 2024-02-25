import xlsxwriter

def generate_excel_file(excel_file_path, combined_data, data1):
    workbook = xlsxwriter.Workbook(excel_file_path)
    worksheet = workbook.add_worksheet('Sheet1')

    # Define colors in hexadecimal format
    white_color_hex = '#FFFFFF'
    grey_color_hex = '#f5f5f5'
    deep_grey_color_hex = '#d7dae1'
    blue_font_hex = '#0b14fe'

    # Define bold format
    bold_format = workbook.add_format({'bold': True})

    # Write combined data to XLSX
    for row_index, row_data in enumerate(combined_data):
        # Choose color based on row index
        if row_index == len(data1):  # Header row
            cell_format = workbook.add_format({'bg_color': deep_grey_color_hex, 'font_color': blue_font_hex})
        elif row_index % 2 == 0:
            cell_format = workbook.add_format({'bg_color': white_color_hex})  # White color
        else:
            cell_format = workbook.add_format({'bg_color': grey_color_hex})  # Grey color

        for col_index, cell_data in enumerate(row_data):
            if row_index == len(data1):  # Header row
                if cell_data == "Task ID":  # Adjust width for "Task Name" header
                    worksheet.set_column(col_index, col_index, 25)  # Set width to 300px (approx.)
                elif cell_data == "Task Name":
                    worksheet.set_column(col_index, col_index, 40)  # Set width for "Start Time" header
                elif cell_data == "Start Time":
                    worksheet.set_column(col_index, col_index, 20)  # Set width for "Start Time" header
                elif cell_data == "Actual Start Time":
                    worksheet.set_column(col_index, col_index, 20)  # Set width for "Actual Start Time" header
                elif cell_data == "Actual End Time":
                    worksheet.set_column(col_index, col_index, 20)  # Set width for "Actual End Time" header
                elif cell_data == "Duration":
                    worksheet.set_column(col_index, col_index, 20)  # Set width for "Duration" header
                elif cell_data == "Status":
                    worksheet.set_column(col_index, col_index, 25)  # Set width for "Status" header
                worksheet.write(row_index, col_index, cell_data, bold_format)
            else:
                worksheet.write(row_index, col_index, cell_data, cell_format)

    # Adjust column widths
    for i, column in enumerate(zip(*combined_data)):
        max_length = max(len(str(cell)) for cell in column)
        worksheet.set_column(i, i, max_length + 5)  # Add a little extra space

    workbook.close()

# Example usage:
# generate_excel_file("example.xlsx", combined_data, data1)
