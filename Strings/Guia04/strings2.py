#Transformar la cadena "Curso de Python" 
#en la cadena "Curso de Programación en Python". 
#Cortar la cadena original, agregarle el literal "Programación en" y concatenar.

frase = "Curso de Python"
subfrase = "Programacion en "
nuevaFrase = ""

print(frase.find("Python")) #Cortar la frase hasta el index donde esta la palabra que queres cortar, recorrer con un for hasta ahi.
for x in range(9):
    nuevaFrase += frase[x] 

print(nuevaFrase + subfrase + "Python")
