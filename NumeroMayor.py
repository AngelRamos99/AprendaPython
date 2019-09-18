numero1 = int(input('Ingrese numero 1: '))
numero2 = int(input('Ingrese numero 2: '))

if numero1 > numero2:
    print(f'{numero1} es mayor que {numero2}')
elif numero2 > numero1:
    print(f'{numero2} es mayor que {numero1}')
else:
    print('Numeros son iguales')
