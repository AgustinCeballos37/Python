fila = int(input("Ingrese el número de fila (0-7):\n"))
columna = int(input("Ingrese el número de columna (0-7):\n"))

if 0 <= fila <= 7 and 0 <= columna <= 7:
    es_blanca = False
    for i in range(8):
        for j in range(8):
            if i == fila and j == columna:
                es_blanca = (i + j) % 2 == 0
                break
        if es_blanca:
            break
    if es_blanca:
        print("La casilla es blanca.")
    else:
        print("La casilla es negra.")
else:
    print("El número de fila o columna debe estar entre 0 y 7.")
