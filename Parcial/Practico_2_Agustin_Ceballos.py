personas = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-01-2000"
]
nombres = []
nacionalidad = []
fechaNacimiento = []
name = []
lastname = []

for persona in personas:
    arreglo = persona.split(",")
    nombres.append(arreglo[0])
    nacionalidad.append(arreglo[1])
    fechaNacimiento.append(arreglo[2])

for nombre in nombres:
    nombreApellido = nombre.split(" ")
    name.append(nombreApellido[0])
    lastname.append(nombreApellido[1])

añoSolicitado = int(input("Ingrese año: "))
for x in range(len(fechaNacimiento)):
    año = fechaNacimiento[x].split("-")
    if añoSolicitado > int(año[2]):
        print(lastname[x])
paisElegido = input("Ingrese país:")
contador = 0
for i in range(len(nacionalidad)):
    pais = nacionalidad[i].split("(")
    if paisElegido == pais[0]:
        contador += 1
print("La cantidad de personas de",paisElegido,"es",contador)
fechaMasReciente = 0
for e in range(len(fechaNacimiento)):
    fechaAño = fechaNacimiento[e].split("-")
    if int(fechaMasReciente) < int(fechaAño[2]):
        fechaMasReciente = fechaAño[2]
for y in range(len(nombres)):
    fechaAño = fechaNacimiento[y].split("-")
    if int(fechaAño[2]) == int(fechaMasReciente):
        print("la persona mas joven de Europe es",name[y])