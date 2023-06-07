#4.	Pasar una palabra a mayúsculas cambiando los caracteres 
#uno por uno usando la tabla ASCII de referencia 
#(googlear la tabla y las funciones de conversión en Python).

palabra = "ñandu"
palabraMayus = ""
for letra in palabra:
    valorASCII = ord(letra)
    valorEnMayus = valorASCII - 32
    letraMayus = chr(valorEnMayus)
    palabraMayus += letraMayus
print(palabraMayus)