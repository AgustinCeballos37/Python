valor = 1
contador = 0
while valor != 0:
    auto = input("Ingrese marca:\n")
    valor = int(input("Ingrese valor del auto:\n"))
    if valor >= 3_460_000 and valor <= 12_850_000:
        contador = contador + 1

print(contador)
