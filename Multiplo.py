numero = int(input('Ingresa un numero: '))

mul3 = (numero % 3)
mul5 = (numero % 5)
mul7 = (numero % 7)

if (mul3 == 0 and mul5 == 0) or (mul7 == 0):
    print('Correcto')
else:
    print('Incorrecto')