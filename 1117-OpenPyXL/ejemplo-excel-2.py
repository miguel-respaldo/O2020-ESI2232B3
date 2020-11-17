import openpyxl

mixls = openpyxl.load_workbook("nuevoExcel.xlsx")

mixls.create_sheet()

print(mixls.get_sheet_names())

mixls.create_sheet(index=0, tittle="1ra hoja")

print(mixls.get_sheet_names())

mixls.create_sheet(index=2, tittle="3ra hoja")

print(mixls.get_sheet_names())

mixls.remove_sheet(mixls.get_sheet_names("1ra hoja"))

hoja = mixls.get_sheet_names("3ra hoja")

hoja["F6"] = "Valor de F6"

print(hoja["F6"].value)
