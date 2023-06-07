#1.	Transformar esta cadena a dos listas paralelas de nombres y sueldos
#(sin el signo pesos): “Juan$120000,Ana$250000,Luis$76500,Vilma$98700”.
# Mostrar las listas resultantes completas.
#Salida esperada: ['Juan', 'Ana', 'Luis', 'Vilma'] [120000, 250000, 76500, 98700]

string = "Juan$120000,Ana$250000,Luis$76500,Vilma$98700"
listOne = []
listTwo = []
nameList = []
jobSalary = [] 
fraseEnLista = string.split(",")

for frase in fraseEnLista:
    fraseNombre, fraseSueldo = frase.split("$") 
    nameList.append(fraseNombre)
    jobSalary.append(fraseSueldo) 

#print(fraseEnListaFix)

print(nameList,jobSalary)
#nameList.append(fraseEnListaFix[1:2])