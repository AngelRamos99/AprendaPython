import random   #Importar biblioteca para generar valores aleatorios

def GeneraNumero1_10():  #Funcion para generar un numero del 1 al 10
    return float(random.randrange(1, 10))

def SumarNumeros(numero1, numero2):  #Funcion para sumar los dos numero y generar mensaje
    suma = float(numero1 + numero2)
    return 'La suma de ' + str(numero1) + ' y ' + str(numero2) + ' es ' + str(suma)

numero1 = float(32.12)   #Declarar primer numero

mensaje = SumarNumeros(numero1, GeneraNumero1_10()) #Generar mensaje
print(mensaje)                                      #Imprimir mensaje

