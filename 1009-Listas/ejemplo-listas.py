# Ejemplo listas

l1 = [7,2,11,4,6,21]
#     0 1 2  3 4 5
l2 = [8,5]

print( len(l1) )
print( max(l1) )
print( min(l1) )
print( sum(l1) )

print( 5 in l1)
print( 11 in l1)
print( 8 not in l1)

print(l1 + l2)

print(l1[3])
print(l1[1:3])

print(3*l2)

l2 = l1
print(l1 == l2)
print(l2)
