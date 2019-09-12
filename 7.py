palabraOriginal = input('Ingrese una palabra: ')
palabraOriginal = palabraOriginal.replace(' ', '')
palabraAlRevez = palabraOriginal[::-1]

if palabraOriginal == palabraAlRevez:
    print(f'La palabra {palabraOriginal} es una palabra palíndroma')
else:
    print(f'La palabra {palabraOriginal} NO es una palabra palíndroma')