#2) Convierte una lista en cadena, solicitando al usuario el separador a utilizar. 
#Ejemplo: 
#lista = [‘quico’, 123, ‘mesa’]
#separador = ‘<->’
#resultado: ‘quico<->123<->mesa’

lista = ["quico", 123, "mesa"]
separador = input("Ingrese el separador a utilizar: ")
resultadoString = ""

for i in range(len(lista)):
    resultadoString += str(lista[i])
    if i != len(lista) - 1:
        resultadoString += separador
print("Resultado:", resultadoString)