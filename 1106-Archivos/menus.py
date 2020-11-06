
def menu11():
    print("Menu  11")
    print("")
    print("1. Menu 111")
    print("2. Menu 112")
    print("")
    print("3. Salir")
    print("")
    opcion = int(input("Opción: "))
    return opcion


def menu111():
    print("Menu  111")
    print("")
    print("1. Menu 1111")
    print("2. Menu 1112")
    print("")
    print("3. Salir")
    print("")
    opcion = int(input("Opción: "))
    return opcion


def menu112():
    print("Menu  112")
    print("")
    print("1. Menu 1121")
    print("2. Menu 1122")
    print("")
    print("3. Salir")
    print("")
    opcion = int(input("Opción: "))
    return opcion


def opciones11():
    opcion = 0
    # mientras opción es diferente de 4
    while opcion != 3:
        opcion = menu11()
        if opcion == 1:
            opciones111()
        elif opcion == 2:
            opciones112()
        elif opcion < 1 or opcion > 3:
            print("Opción Invalida")
            print("")


def opciones111():
    opcion = 0
    # mientras opción es diferente de 4
    while opcion != 3:
        opcion = menu111()
        if opcion == 1:
            print("Opción 1111")
        elif opcion == 2:
            print("Opción 1112")
        elif opcion < 1 or opcion > 3:
            print("Opción Invalida")
            print("")


def opciones112():
    opcion = 0
    # mientras opción es diferente de 4
    while opcion != 3:
        opcion = menu112()
        if opcion == 1:
            print("Opción 1121")
        elif opcion == 2:
            print("Opción 1122")
        elif opcion < 1 or opcion > 3:
            print("Opción Invalida")
            print("")


def menu1():
    print("Menu  1")
    print("")
    print("1. Menu 11")
    print("2. Menu 12")
    print("3. Menu 13")
    print("4. Menu 14")
    print("")
    print("5. Salir")
    print("")
    opcion = int(input("Opción: "))
    return opcion


def principal():
    opcion = 0

    # mientras opción es diferente de 4
    while opcion != 5:

        opcion = menu1()

        if opcion == 1:
            opciones11()
        elif opcion == 2:
            print("opcion 2")
        elif opcion == 3:
            print("opcion 3")
        elif opcion == 4:
            print("opcion 4")
        elif opcion < 1 or opcion > 5:
            print("Opción Invalida")
            print("")



if __name__ == "__main__":
    principal()
