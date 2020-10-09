import random
# La computadora piensa un número
numero_compu = random.randint(1, 10)
# El usuario introduce un  número
numero_usuario = int(input("Adivina el número: "))

# Mientras el usuario no adivine el numero
# preguntar por un nuevo numero

while not numero_compu == numero_usuario:
    print("Intentalo nuevamente (",numero_compu,")")
    numero_usuario = int(input("Adivina el número: "))

print("Adivinaste es el ",numero_compu)
