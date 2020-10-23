archivo = open("prueba2.csv","w")

#lineas = ["linea no. 1\n", "linea no. 2\n", "linea no. 3"]
lineas = ["Producto,precio\n", "agua,5\n", "coca,10\n", "tortillas,15\n", "platanitos,10"]

archivo.writelines(lineas)

print("Se escribio el archivo")
