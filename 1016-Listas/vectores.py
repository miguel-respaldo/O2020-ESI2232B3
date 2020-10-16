# Vectores

def suma_vector():
    v1 = []
    v2 = []
    res = []

    print("Introduce los valores del primer vector: ")
    for i in range(3):
        numero = float(input("Escribe el valor " + str(i+1) + ": "))
        v1.append(numero)

    print("Introduce los valores del segundo vector: ")
    for i in range(3):
        numero = float(input("Escribe el valor " + str(i+1) + ": "))
        v2.append(numero)

    for i in range(3):
        numero = v1[i] + v2[i]
        res.append(numero)

    print("El resultado es:", res)
    print("")


def resta_vector():
    v1 = [0, 0, 0]
    v2 = [0, 0, 0]
    res = [0, 0, 0]

    print("Introduce los valores del primer vector: ")
    for i in range(3):
        v1[i] = float(input("Escribe el valor " + str(i+1) + ": "))

    print("Introduce los valores del segundo vector: ")
    for i in range(3):
        v2[i] = float(input("Escribe el valor " + str(i+1) + ": "))

    for i in range(3):
        res[i] = v1[i] - v2[i]

    print("El resultado es:", res)
    print("")



def menu():
    print("Menu de calculadora de vectores")
    print("")
    print("1. Suma")
    print("2. Resta")
    print("3. Producto punto")
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
        suma_vector()
    elif opcion == 2:
        resta_vector()
    elif opcion == 3:
        print("opción 3")
    elif opcion < 1 or opcion > 4:
        print("Opción Invalida")
        print("")

