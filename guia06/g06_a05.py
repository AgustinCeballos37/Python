def inputStr():
    
    validado = False
    numeros = "1","2","3","4","5","6","7","8","9","0"
    digitos = "#", "$","%","&"
    while not validado:
        cadena = input("ingrese un nombre de usuario: ")
        if len(cadena) >= 8:
            checkerCaracterEspecial = False
            checkerNumero = False 
            for caracter in cadena:
                if caracter in numeros:
                    checkerNumero = True
                if caracter in digitos:
                    checkerCaracterEspecial = True

            if checkerNumero and checkerCaracterEspecial == True:
                validado = True
                print("validado")
                return cadena
            else:
                print("tiene que llevar un caracter especial y un numero")
                print("Caracter:",checkerCaracterEspecial, "\nNumero: ",checkerNumero)
        else:
            print("tiene que tener un largo de 8 caracteres o mas")

inputStr()