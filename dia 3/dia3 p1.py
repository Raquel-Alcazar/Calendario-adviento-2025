
####PARTE 1####

fichero = open('dia 3\\archivo3.txt')
lineas = fichero.readlines()

contador = 0

for i in lineas:
    bateria = i.strip()
    maximo1 = bateria[0]

    for num in bateria[:-1]:
        if num > maximo1:
            maximo1 = num
    aux = bateria[bateria.index(maximo1)+1:]
    maximo2 = aux[0]

    for num in aux:
        if num > maximo2:
            maximo2 = num

    voltios = maximo1 + maximo2
    contador = contador + int(voltios)
    
print('Voltios totales: ', contador)

