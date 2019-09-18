print('Tablas del 1 al 10')
print('_______________________________________')
print('')
for i in range(1, 11):
    titulo = 'Tabla del {}'
    print(titulo.format(i))
    print('')
    
    for e in range(1, 11):
        mensaje = '{} x {} = {}'
        print(mensaje.format(i, e, e * i))
    
    print('_______________________________________')
