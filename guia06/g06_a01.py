def concatenar(*args, conector=" "):
    stringFinal = ""
    for i in range(len(args)):
        stringFinal += args[i]
        if i != len(args) - 1:
            stringFinal += conector
    return stringFinal

print(concatenar('hola', 'pibe'))
print(concatenar('hola', 'pibe', conector='@'))
print(concatenar('techo', 'mesa', 'árbol', conector='###'))
print(concatenar('techo', 'mesa', 'árbol', conector='|||||||'))