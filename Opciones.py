opcion = input('Ingrese "a", "b" o "c": ')
opcionesVal = ('a', 'b', 'c', 'A', 'B', 'C')

while opcion not in opcionesVal:
    opcion = input('Opcion invalida. Ingrese "a", "b" o "c": ')

print('Opcion correcta.')
