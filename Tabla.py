numero = int(input('Que tabla quieres generar? '))

for i in range(1, 11):
    mensaje = '{} x {} = {}'
    print(mensaje.format(numero, i, numero * i))
