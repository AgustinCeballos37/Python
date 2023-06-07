#Mostrar el valor doble del número de dos cifras (que es el único número) 
#encontrado en la cadena. Ej.: 'Juan tiene 25 años' mostraría el número 50, 
#‘El dólar va a llegar este mes a 500 pesos casi seguro’,  mostraría 1000

frase = "Juan tiene 25 años"
numeros = ["0","1","2","3","4","5","6","7","8","9","0"]
numero1 = 0
numero2 = 0

for palabra in frase:
    if palabra in numeros:
        numero1 = int(palabra)
for palabra in frase:
    if palabra in numeros and int(palabra) != numero1:
        numero2 = int(palabra)
#devuelve los numeros dados vuelta
numeroSacadoDeString = str(numero2) + str(numero1) #por eso numero2 adelante
multiplicadoX2 = (int(numeroSacadoDeString) * 2) 

print(multiplicadoX2)