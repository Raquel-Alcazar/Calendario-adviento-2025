
####PARTE 1####

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
        if(len(str(i))%2 == 0):
            primera_mitad = str(i)[:punto_medio]
            segunda_mitad = str(i)[punto_medio:]
            if primera_mitad == segunda_mitad:
                #print("mitades iguales")
                contador = contador + i
            

print("Contador final es: ", contador)


    





