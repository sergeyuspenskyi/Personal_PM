from openpyxl import load_workbook
wb = load_workbook('example.xlsx')
worksheet = wb.active
sheet_list = [{cell.coordinate: cell.value for cell in row_cells} for row_cells in worksheet.iter_rows()]
print(sheet_list)