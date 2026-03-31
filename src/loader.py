from openpyxl import load_workbook

def load(df, country_name):
    file_name = country_name.replace(" ", "_")
    file_path = f"output/{file_name}_top10.xlsx"
    df.to_excel(file_path, index=False)

    wb = load_workbook(file_path)
    ws = wb.active
    for row in ws.iter_rows(min_row=2, min_col=5, max_col=5):
        for cell in row:
            cell.number_format = '#,##0.00'
    wb.save(file_path)
    