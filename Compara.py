numero1 = int(input('Ingrese numero 1: '))
numero2 = int(input('Ingrese numero 2: '))

mensaje1 = 'Numeros proporcionados: ' + str(numero1) + ' y ' + str(numero2) + '.'
mensaje2 = ''

if numero1 == numero2:
    mensaje2 = 'Los numeros son iguales.'
else:
    if numero1 > numero2:
        mensaje2 = 'El mayor es el primero.'
    else:
        mensaje2 = 'El mayor es el segundo.'

mensaje = mensaje1 + ' ' + mensaje2
print(mensaje)