from openpyxl import load_workbook


def get_file_content(filename) -> list:
    """Returns list with dicts per row in scrapped excel file"""
    wb = load_workbook(filename)
    worksheet = wb.active
    sheet_list = [{cell.coordinate: cell.value for cell in row_cells} for row_cells in worksheet.iter_rows()]
    return sheet_list
