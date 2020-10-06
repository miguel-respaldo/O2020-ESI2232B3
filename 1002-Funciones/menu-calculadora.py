import math


def area_rectangulo():
    base=float(input("Escribe la base: "))
    altura= float(input("Escribe la altura: "))
    area = base * altura;
    print("El área es:", area)
    print("")


def area_triangulo(base, altura):
    area = base * altura / 2
    return area


def area_circulo():
    radio = float(input("Escribe el radio: "))
    area = math.pi * radio * radio
    print("El área es:", area)
    print("")


def menu():
    print("Menu de calculadora")
    print("")
    print("1. Área de rectángulo")
    print("2. Área de tríangulo")
    print("3. Área de cuadrado")
    print("4. Área de círculo")
    print("")
    print("5. Salir")
    print("")
    opcion = int(input("Opción: "))
    return opcion


opcion = 0

# mientras opción es diferente de 5
while opcion != 5:

    opcion = menu()

    if opcion == 1:

        area_rectangulo()

    elif opcion == 2:
        base=float(input("Escribe la base: "))
        altura= float(input("Escribe la altura: "))

        area = area_triangulo(base, altura)

        print("El área es:", area)
        print("")
    elif opcion == 3:

        area_rectangulo()

    elif opcion == 4:

        area_circulo()

    elif opcion < 1 or opcion > 5:
        print("Opción Invalida")
        print("")

