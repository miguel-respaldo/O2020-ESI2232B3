import random

# Defininen 3 funciones sujeto, verbo y objeto
def sujeto():
    numero = random.randint(1,3)
    cadena = ""

    if numero == 1:
        cadena = "La casa"
    elif numero == 2:
        cadena = "La bodega"
    else:
        cadena = "El carro"

    return cadena


def verbo():
    numero = random.randint(1,3)

    if numero == 1:
        return "es"
    elif numero == 2:
        return "está"
    else:
        return "tiene"


def objeto():
    numero = random.randint(1,3)
    cadena = ""

    if numero == 1:
        cadena = "grande"
    elif numero == 2:
        cadena = "fea"
    else:
        cadena = "bonita"

    return cadena


print(sujeto(),verbo(),objeto())
