import openpyxl

mixls = openpyxl.Workbook()

print(mixls.get_sheet_names())

hoja = mixls.active

print(hoja.title)

hoja.title = "Nuevo nombre"

print(mixls.get_sheet_names())

mixls.save("nuevoExcel.xlsx")



