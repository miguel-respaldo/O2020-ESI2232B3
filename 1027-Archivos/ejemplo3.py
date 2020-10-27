import csv

nombre_archivo = str(input("Escribe el nombre del archivo: "))
archivo = open(nombre_archivo,"a")

escritor = csv.writer(archivo)

fila=[]
for i in range(3):
    celda = input("Escribe la celda "+str(i+1)+": ")
    fila.append(celda)

escritor.writerow(fila)
