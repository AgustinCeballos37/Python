masEmpleados = ""
totalSueldo = 0
while masEmpleados != "no":
    montoSueldos = int(input("Ingrese el monto del sueldo:\n"))
    totalSueldo = totalSueldo + montoSueldos
    masEmpleados = input("Hay mas empleados para agregar?\n")
print("El total es ",totalSueldo)

