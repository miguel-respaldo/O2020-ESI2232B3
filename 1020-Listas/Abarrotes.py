
productos = ["platanitos","crema", "sabritones","tortillas", "cocas", "frutas"]
precios =   [15.0,          20.0,   15.0,         10.0,     7.5, 5.5   ]
cantidad =  [8,             4,      8,             3,       5,  7 ]

def imprimir_productos():
    tamanio = len(productos)
    print("Producto   Cantidad  Precio")
    print("---------------------------------")
    for i in range(tamanio):  # 5 ->  0,1,2,3,4
        print(productos[i] + "   " + str(cantidad[i]) + "    " + str(precios[i]))
    print("")


def comprar():
    tamanio = len(productos)
    for i in range(tamanio):  # 5 ->  0,1,2,3,4
        print(str(i+1) + ".- " +productos[i])
    print("")
    num_prod = int(input("Cual producto vas a comparar?: "))
    cantidad[num_prod-1] = cantidad[num_prod-1] - 1


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


opcion = 0

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

