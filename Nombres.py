cantidad = int(input('Ingrese cantidad de nombres por capturar: '))
nombres = []

for i in range(1, cantidad + 1):
    nombre = input('Ingrese nombre ' + str(i) + ': ')
    nombres.append(nombre)

mensaje = 'Nombres ingresados: '

for nombre in nombres:
    if mensaje == 'Nombres ingresados: ':
        mensaje = mensaje + nombre
    else:
        mensaje = mensaje + ', ' + nombre

print(mensaje)
