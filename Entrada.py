numero = input('Ingresa un numero entero: ')  #Pedir valor
print(type(numero))                           #Imprimir el tipo de dato (str)

valido = True  #Generar flag de numero valido

for caracter in numero:  #Por cada caracter en valor ingresado
    if caracter not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):  #Verificar que este en los valores permitidos de numero entero
        valido = False  #Caracter fuera de rango, desactivar flag
        break           #Salir

if valido == True:   #Valor es entero
    numero = int(numero)
    print('Dato entero. ¡Muy bien!')
else:
    print('Dato no es entero. Intentar nuevamente.')
