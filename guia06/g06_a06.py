from g06_a06lib import inputInt, inputFloat, inputNumber

q = inputInt("Ingrese un numero", minimo=10, maximo=50)

m = inputFloat("ingrese un float")

r = inputNumber(float,"ingrese un numero", minimo=500,maximo=800)

print(q,m,r)