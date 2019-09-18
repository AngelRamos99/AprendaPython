def EsNumero(numero):
    for caracter in numero:
        if caracter not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return False
    return True

suma = 0

while True:
    numero = input('Ingresa un numero: ')
    if numero == '':
        salida = 'Suma acumulada: {}.'
        print(salida.format(suma))
        break
    else:
        if EsNumero(numero):
            suma = suma + int(numero)
            print('Monto acumulado correctamente.')
        else:
            print('Numero no valido. Ingresa otro.')