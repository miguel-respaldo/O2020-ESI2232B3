archivo = open("prueba4.txt", 'r')

# lee el archivo completo
#contenido = archivo.read()

contenido = archivo.readline()
print(contenido,end="")

contenido = archivo.readline()
print(contenido, end="")

contenido = archivo.readline()
print(contenido)
