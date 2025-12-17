
####PARTE 1####

fichero = open('dia 4\\archivo4.txt')
lineas = fichero.readlines()

contador = 0
total = 0
mosaico = []

for i in lineas:
    bateria = i.strip()
    mosaico.append(bateria)

for i in range(len(mosaico)):
    for j in range(len(mosaico)):
        contador = 0
        print(f"Estoy en fila {i} columna {j} ")
        celda = mosaico[i][j]
        if celda == "@":
            print("La celda es igual a: ", celda)
            if j + 1 < len(mosaico[i]) and mosaico[i][j + 1] == "@": #Derecha
                contador = contador + 1 
                print("Tengo a la derecha")
            if j - 1 >= 0 and mosaico[i][j - 1] == "@": #Izquieda
                contador = contador + 1
                print("Tengo a la izquieda")
            if i - 1 >= 0 and mosaico[i - 1][j] == "@": #Arriba
                contador = contador + 1
                print("Tengo arriba")
            if i + 1 < len(mosaico) and mosaico[i + 1][j] == "@": #Abajo
                contador = contador + 1
                print("Tengo abajo")
            if i - 1 >= 0 and j + 1 < len(mosaico[i]) and mosaico[i - 1][j + 1] == "@": #Arriba-Derecha
                contador = contador + 1
                print("Tengo arriba-derecha")
            if i - 1 >= 0 and j - 1 >= 0 and mosaico[i - 1][j - 1] == "@": #Arriba-Izquieda  
                contador = contador + 1
                print("Tengo arriba-izquieda")
            if i + 1 < len(mosaico) and j + 1 < len(mosaico[i]) and mosaico[i + 1][j + 1] == "@": #Abajo-Derecha  
                contador = contador + 1
                print("Tengo abajo-derecha")
            if i + 1 < len(mosaico) and j - 1 >= 0 and mosaico[i + 1][j - 1] == "@": #Abajo-Izquieda  
                contador = contador + 1
                print("Tengo abajo-izquierda")
            
            if(contador < 4):
                total = total + 1
                print("Contador total actualizado: ", total)
                print("")
                print(f"ESTA POSICIÓN ES UNA DE LAS BUSCADAS [{i}][{j}]")
                print("")
    print("-------------------------------")
print("El total del rollos es: ", total)


