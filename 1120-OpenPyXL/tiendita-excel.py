import openpyxl

archivo = ""
hoja = ""

def abrir():
    global archivo
    global hoja
    archivo = openpyxl.load_workbook("productos.xlsx")
    hoja = archivo["productos"]


def imprimir_productos():
    print("Producto   Cantidad   Precio")
    print("---------------------------------")
    for fila in hoja.values:
        # Este if es para no imprimir la cabecera (la fila 1)
        if fila[0] == "producto" or fila[0] == "borrado":
            continue
        print(fila[0] + "   " + str(fila[2]) + "    " + str(fila[1]))
    print("")


def comprar():
    contador=1
    num_producto=0
    lista=[]
    for fila in hoja.values:
         # Este if es para no imprimir la cabecera (la fila 1)
        if fila[0] == "producto":
            continue
        print(str(contador) + ".- " + fila[0])
        lista.append(fila[0])
        contador = contador+1
    print("")

    producto = str(input("¿Cual producto quieres comparar?: "))
    # Verifico si es número o texto
    if producto.isnumeric():
        num_producto=int(producto)
        if num_producto < 1 or num_producto > contador-1:
            print("El producto no existe.")
            print("")
            return
        else:
            producto = lista[num_producto-1]

    if producto not in lista:
        print("El producto no existe")
        print("")
        return

    cantidad = int(input("Cantidad de producto: "))

    if cantidad < 1:
        print("La cantidad es invalida.")
        print("")
        return

    for fila in range(contador-1):
        # Si el producto es el que estoy buscando
        if hoja["A"+str(fila+1)].value == producto:
            # Verifico si tengo suficiente producto
            if cantidad > int(hoja["C"+str(fila+1)].value):
                print("No hay suficiente producto")
            else:
                # Resto de mi stock la cantidad
                hoja["C"+str(fila+1)] = int(hoja["C"+str(fila+1)].value) - cantidad

    archivo.save("productos.xlsx")



def surtir():
    contador=1
    num_producto=0
    lista=[]

    for fila in hoja.values:
         # Este if es para no imprimir la cabecera (la fila 1)
        if fila[0] == "producto":
            continue
        print(str(contador) + ".- " + fila[0])
        lista.append(fila[0])
        contador = contador+1
    print("")

    producto = str(input("¿Cual producto quieres surtir?: "))
    # Verifico si es número o texto
    if producto.isnumeric():
        num_producto=int(producto)
        if num_producto < 1 or num_producto > contador-1:
            print("El producto no existe.")
            print("")
            return
        else:
            producto = lista[num_producto-1]

    if producto not in lista:
        print("El producto no existe")
        print("")
        return

    cantidad = int(input("Cantidad de producto a surtir: "))

    if cantidad < 1:
        print("La cantidad es invalida.")
        print("")
        return

    for fila in range(contador-1):
        # Si el producto es el que estoy buscando
        if hoja["A"+str(fila+1)].value == producto:
            # Verifico si tengo suficiente producto
            if cantidad > int(hoja["C"+str(fila+1)].value):
                print("No hay suficiente producto")
            else:
                # Resto de mi stock la cantidad
                hoja["C"+str(fila+1)] = int(hoja["C"+str(fila+1)].value) + cantidad

    archivo.save("productos.xlsx")


def quitar():
    contador=1
    num_producto=0
    lista=[]

    for fila in hoja.values:
         # Este if es para no imprimir la cabecera (la fila 1)
        if fila[0] == "producto":
            continue
        print(str(contador) + ".- " + fila[0])
        lista.append(fila[0])
        contador = contador+1
    print("")

    producto = str(input("¿Cual producto quieres quitar?: "))
    # Verifico si es número o texto
    if producto.isnumeric():
        num_producto=int(producto)
        if num_producto < 1 or num_producto > contador-1:
            print("El producto no existe.")
            print("")
            return
        else:
            producto = lista[num_producto-1]

    if producto not in lista:
        print("El producto no existe")
        print("")
        return

    for fila in range(contador-1):
        # Si el producto es el que estoy buscando
        if hoja["A"+str(fila+1)].value == producto:
            # Verifico si tengo suficiente producto
            hoja["A"+str(fila+1)] = "borrado"
            hoja["B"+str(fila+1)] = "borrado"
            hoja["C"+str(fila+1)] = "borrado"

    archivo.save("productos.xlsx")


def agregar():
    global archivo
    nuevo_producto = ["nombre","precio","cantidad"]
    # Pedir al usuario el producto
    nuevo_producto[0] = str(input("Escribe el nombre del producto: "))
    # Pedir al usuario la cantidad
    nuevo_producto[2] = str(input("Escribe la cantidad del producto: "))
    # Pedir al usuario el precio
    nuevo_producto[1] = str(input("Escribe el precio del producto: "))
    # Abrir archivo para agregar al Final

    contador=1
    for fila in hoja.values:
        contador = contador+1

    hoja["A"+str(contador)] = nuevo_producto[0]
    hoja["B"+str(contador)] = float(nuevo_producto[1])
    hoja["C"+str(contador)] = int(nuevo_producto[2])

    archivo.save("productos.xlsx")


def menu():
    print("Menu de Productos")
    print("")
    print("1. Imprimir productos")
    print("2. Comparar algun producto")
    print("3. Surtir producto")
    print("4. Agregar producto")
    print("5. Quitar  producto")
    print("")
    print("6. Salir")
    print("")
    opcion = int(input("Opción: "))
    return opcion


def principal():
    opcion = 0
    # Abrir el archivo a usar
    abrir()
    # mientras opción es diferente de 4
    while opcion != 6:

        opcion = menu()

        if opcion == 1:
            imprimir_productos()
        elif opcion == 2:
                comprar()
        elif opcion == 3:
            surtir()
        elif opcion == 4:
            agregar()
        elif opcion == 5:
            quitar()
        elif opcion < 1 or opcion > 6:
            print("Opción Invalida")
            print("")



if __name__ == "__main__":
    principal()
