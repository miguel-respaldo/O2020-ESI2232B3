lista=[1,2,3,4,5,1,2,4,5,6,1,2]

print(lista)
elemento = int(input("Escribe el elemento a borrar: "))

# mientras exista el elemento en lista
# borrar o remover ese elemento

while elemento in lista:
    lista.remove(elemento)

print(lista)
