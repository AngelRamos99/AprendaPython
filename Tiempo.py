def CalcularTiempo(vel, dis):
    ValorTiempo = dis / vel
    return ValorTiempo

velocidad = float(input('Ingrese velocidad en Km/h: '))
distancia = float(input('Ingrese distancia en Km: '))

tiempo = CalcularTiempo(velocidad, distancia)

print(f'El tiempo requerido es de {tiempo} horas.')
