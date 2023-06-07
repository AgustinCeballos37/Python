def funcioncita():
    print("Hola amigo")
funcioncita()
def otraFuncion():
    return "Prueba"
print(otraFuncion())
def suma(x, y):
    return x+y
print(suma(4,5))
def resta(x,y):
    return x-y
print(resta(5,4))
def division(x,y):
    return x/y
print(division(12,4))
def multiplicacion(x,y):
    return x*y
print(multiplicacion(5,4))

x = int(input("Ingrese un numero: "))
y = int(input("Ingrese otro Numero: "))
print("1_ Sumar")
print("2_ Restar")
print("3_ Multiplicar")
print("4_ Dividir")
selectorDeOperacion = int(input("Ingrese la operacion a realizar: "))
if selectorDeOperacion == 1:
    print(suma(x,y))
elif selectorDeOperacion == 2:
    print(resta(x,y))
elif selectorDeOperacion == 3:
    print(multiplicacion(x,y))
elif selectorDeOperacion == 4:
    print(division(x,y))
else:
    print("No se encontro la operacion. ")