#La salida esperada que se muestre por pantalla, debería ser la siguiente: 

#Iniciales y apellido de las personas: 
#A. Torres
#K. Hudson
#B. Quesada
#S. Campoamores
#C. Santamaría
#A. Skarsgard
#W. Catalejos

#El nombre más largo es: Benicio}

#El promedio de edad de las mujeres es: 50

nombres = [
        "Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio",
        "Campoamores, Susana", 
        "Santamaría, Carlos",
        "Skarsgard, Azul", 
        "Catalejos, Walter"
        ] 
sexos = ["f","f","m","f","m","f","m"]
fechas = [
"02/05/1943",
"07/09/1984",
"10/02/1971",
"21/12/1967",
"30/01/1982",
"30/08/1995",
"18/07/1959"
]


for nombre in nombres:
    serapadosPorComa = nombre.split(",")
    inicialNombre = serapadosPorComa[1]
    print(inicialNombre[1] + "." + " " + serapadosPorComa[0])
    #print(serapadosPorComa)
listanueva = []
for nombre in nombres:
    serapadosPorComa = nombre.split(",")
    inicialNombre = serapadosPorComa[1]
    listanueva.append(inicialNombre)
masLargo = 0
nombreMasLargo = ""

for nombre in listanueva:
    if len(nombre) > len(nombreMasLargo):
        nombreMasLargo = nombre
print("El nombre mas largo es:",nombreMasLargo)
edades=[]
for x in range(len(fechas)):
    if sexos[x] == "f":
        fechaAcual = 2023
        separadas = fechas[x].split("/")
    #print(separadas)
        fechaNacimiento = separadas[2]
        edad = fechaAcual - int(fechaNacimiento)
        
        edades.append(edad)
sumaTodasEdades = 0
for edad in edades:
    sumaTodasEdades += edad
promedio = sumaTodasEdades / (len(edades))
print("El promedio de edad de las mujeres es:",int(promedio))