#Calcula dónde estará un robot (sus coordenadas finales) que se encuentra en una cuadrícula 
#representada por los ejes "x" e "y".
#El robot comienza en la coordenada (0, 0).
#Para indicarle que se mueva, le enviamos una lista formada por enteros  
#(positivos o negativos) que indican la secuencia de pasos a dar.
#Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene,   luego 5, se detiene, y finalmente 2. 

#El resultado en este caso sería (x: -5, y: 12) #erroneo

# Si el número de pasos es negativo, se desplazaría en sentido contrario al  que está mirando (camina hacia atrás)
# Los primeros pasos los hace en el eje "y". Interpretamos que está mirando  hacia la parte positiva del eje "y".
# El robot tiene un fallo en su programación: cada vez que finaliza una   secuencia de pasos gira 90 grados en el sentido contrario a las agujas del reloj.

listaPasos = [10, 5, -2]
x = 0
y = 0
direccion = 1   

for pasos in listaPasos:
    if direccion == 1:
        y += pasos
    else:
        x += pasos
    direccion *= -1   #bug girar 90 grados 
print("x:",x,"y:",y)