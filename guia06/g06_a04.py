def inputStr():

    validado = False
    while not validado: 
        cadena = input("ingrese una cadena de mas de 8 caracteres: ")
        if len(cadena) >= 8:
            validado = True
            print("validado")
        else:
            print("no cumple")

inputStr()