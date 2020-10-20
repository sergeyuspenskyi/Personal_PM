from openpyxl import load_workbook
wb = load_workbook('example.xlsx')
sheet = wb.active
for cellObj in sheet['A1':'E11']:
    for cell in cellObj:
        result = {cell.coordinate: cell.value}
        print(result)