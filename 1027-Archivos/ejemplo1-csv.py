#  CSV es Comma Separated Values
import csv

nombre_archivo = str(input("Escribe el nombre del archivo: "))
archivo = open(nombre_archivo,"r")

lector = csv.reader(archivo)

for fila in lector:
    fila_cadena="   ".join(fila)
    print(fila_cadena)

print("**************************")
## Regresamos el archivo a la posición inicial
archivo.seek(0)

for fila in lector:
    print("Columna 1: " + fila[0])
    print("Columna 2: " + fila[1])
    print("Columna 3: " + fila[2])

# Cierra el archivo
archivo.close()
