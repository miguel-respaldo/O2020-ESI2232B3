import csv

archivo = ""
lector = ""

def abrir():
    global archivo
    global lector
    archivo = open("productos.csv","r")
    lector = csv.reader(archivo)


def imprimir_productos():
    print("Producto   Cantidad   Precio")
    print("---------------------------------")
    # Me salto una linea que es la cabecera del archivo CSV
    next(lector)
    for fila in lector:
        print(fila[0] + "   " + str(fila[2]) + "    " + str(fila[1]))
    print("")
    # Hay que regresar al principio
    archivo.seek(0)


def comprar():
    # Nos saltamos la primera linea
    next(lector)
    contador=1
    num_producto=0
    lista=[]
    for fila in lector:
        print(str(contador) + ".- " + fila[0])
        lista.append(fila[0])
        contador = contador+1
    print("")
    archivo.seek(0)
    producto = str(input("¿Cual producto quieres comparar?: "))
    # Verifico si es número o texto
    if producto.isnumeric():
        num_producto=int(producto)
        if num_producto < 1 or num_producto > contador-1:
            print("El producto no existe.")
            return
        else:
            producto = lista[num_producto-1]

    if producto not in lista:
        print("El producto no existe")
        return

    cantidad = int(input("Cantidad de producto: "))

    archivo_temporal = open("temporal.csv","w")
    escritor=csv.writer(archivo_temporal)
    for fila in lector:
        if fila[0] == producto:
            print("si es igual")
            escritor.writerow(fila)
        else:
            escritor.writerow(fila)
    archivo_temporal.close()






def surtir():
    tamanio = len(productos)
    for i in range(tamanio):  # 5 ->  0,1,2,3,4
        print(str(i+1) + ".- " +productos[i])
    print("")
    num_prod = int(input("Cual producto vas a surtir?: "))
    cantidad[num_prod-1] = cantidad[num_prod-1] + 1


def menu():
    print("Menu de Productos")
    print("")
    print("1. Imprimir productos")
    print("2. Comparar algun producto")
    print("3. Surtir producto")
    print("")
    print("4. Salir")
    print("")
    opcion = int(input("Opción: "))
    return opcion


def principal():
    opcion = 0
    # Abrir el archivo a usar
    abrir()
    # mientras opción es diferente de 4
    while opcion != 4:

        opcion = menu()

        if opcion == 1:
            imprimir_productos()
        elif opcion == 2:
            comprar()
        elif opcion == 3:
            surtir()
        elif opcion < 1 or opcion > 4:
            print("Opción Invalida")
            print("")



if __name__ == "__main__":
    principal()
