
####PARTE 2####

minimo = 0
maximo = 0
contador = 0

fichero = open("dia 2\\archivo2.txt")
linea = fichero.readlines()
fichero.close()
rangos = linea[0].split(",")
#print(rangos[0])
#print(rangos[0].split("-"))


for i in rangos:
    rango = i.split("-")
    #print(rango)
    minimo = int(rango[0])
    maximo = int(rango[1])+1
    for i in range(minimo, maximo):
        #print(contador)
        longitud = len(str(i))
        punto_medio = longitud // 2
        #print(i)
        #print(str(i)[0:2])

        divisores = []
        longitud = len(str(i))
        for j in range(1, longitud):
            #print(j)
            if len(str(i))%j == 0:
                divisores.append(j)
        #print("el numero es: ", i)
        #print("LOS DIVISORES SON: ", divisores)
        for j in divisores:
            separados = []
            for k in range(0, len(str(i)), j):
                separados.append(str(i)[k:k+j])
            #print(separados)
            son_iguales = all(x == separados[0] for x in separados)
                
            if son_iguales:
                contador = contador + i
                print("Inválido: ", i)
                break
                
print("Contador final es: ", contador)


    





