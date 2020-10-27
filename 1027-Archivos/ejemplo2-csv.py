import csv

nombre_archivo = str(input("Escribe el nombre del archivo: "))
archivo = open(nombre_archivo,"w")

escritor = csv.writer(archivo)

fila1=["Titulo1", "Titulo2", "Titulo3"]
fila2=["art1","art2","art3"]
fila3=["arta","artb","artc"]

archivo.write(",".join(fila1)+"\n")
archivo.write(",".join(fila2)+"\n")

escritor.writerow(fila3)
escritor.writerow(fila2)

archivo.close()
archivo = open(nombre_archivo,"r")

lector = csv.reader(archivo)

for fila in lector:
    fila_cadena="   ".join(fila)
    print(fila_cadena)

