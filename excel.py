import openpyxl

def fill_excel(file_path, data_list, departure, arrival ):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb["Штурманский журнал"]
    sheet['C11'] = departure
    sheet['C12'] = arrival
    start_row = 23
    for i, data in enumerate(data_list):
        row = start_row + i
        sheet[f"B{row}"] = data.get("ident", "")
        sheet[f"C{row}"] = data.get("hdg", "")
        sheet[f"D{row}"] = data.get("wind_degree_m_kts", "")
        sheet[f"E{row}"] = data.get("head_or_tailwind_kts", "")
        sheet[f"H{row}"] = data.get("distance_nm", "")
    new_file_path = f"{departure}-{arrival}.xlsx"
    wb.save(new_file_path)
    return new_file_path
