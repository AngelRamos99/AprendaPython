numero = '32434'     #Numero en una variable de texto
print(type(numero))  #Imprime el tipo de dato

numero = int(numero) #Convierte la variablea tipo de numero entero
print(type(numero))  #Imprime el nuevo tipo de dato

mensaje = 'El numero convertido fue {}' #Hacer mensaje
print(mensaje.format(numero))           #Imprimir mensaje