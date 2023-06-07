# Dada una lista de nombres y de salarios respectivos, determinar el salario mínimo y mostrar el nombre de la persona que menos gana.


cantidadDeEmpleados = int(input("Ingrese la cantidad de empleados:\n"))
nombreMenosGana = ""
menorSalario = 0
for x in range(cantidadDeEmpleados):
    nombre = input("Ingrese nombre:\n")
    salario = int(input("Ingresar el salario:\n"))
    
    if menorSalario == 0 or salario < menorSalario:
        menorSalario = salario
        nombreMenosGana = nombre

print("El que menos gana es", nombreMenosGana, "con un sueldo de", menorSalario)
    
