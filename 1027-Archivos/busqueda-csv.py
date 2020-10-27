#  CSV es Comma Separated Values
import csv

archivo = open("ejemplo-busqueda.csv","a")

escritor = csv.writer(archivo)

numero = int(input("Número de elementos a Ingresar: "))

for i in range(numero):
    fila=[]
    elemento=input("Nombre del elemento: ")
    cantidad=int(input("Cantidad de elementos: "))
    fila.append(elemento)
    fila.append(cantidad)
    escritor.writerow(fila)

# Escribe en el Disco duro lo de memoria
#archivo.flush()
archivo.close()
archivo = open("ejemplo-busqueda.csv","r")

elemento = input("¿Que elemento quieres buscar?")

lector = csv.reader(archivo)
#archivo.seek(0)

for fila in lector:
    if fila[0] == elemento:
        print("Su cantidad es",fila[1])

