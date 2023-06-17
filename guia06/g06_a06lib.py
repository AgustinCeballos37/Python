def inputInt(mensaje, x=None, y=None, maximo=None, minimo=None):
    validado = False
    
    while not validado:
        try:
            n = int(input(mensaje+" "))
            
            if x is not None and y is not None:
                if n >= x and n <= y:
                    validado = True
                    return n
                else:
                    print(f"el valor debe estar entre {x} y {y}")
            elif minimo is not None and n < minimo:
                print(f"el valor debe ser mayor o igual a {minimo}")
            elif maximo is not None and n > maximo:
                print(f"el valor debe ser menor o igual a {maximo}")
            else:
                validado = True
                return n
        except:
            print('no es entero, intente de nuevo!')
   

def inputFloat(mensaje, x=None, y=None, maximo=None, minimo=None):
    validado = False
    
    while not validado:
        try:
            n = float(input(mensaje+" "))
            
            if x is not None and y is not None:
                if n >= x and n <= y:
                    validado = True
                else:
                    print(f"el valor debe estar entre {x} y {y}")
            elif minimo is not None and n < minimo:
                print(f"el valor debe ser mayor o igual a {minimo}")
            elif maximo is not None and n > maximo:
                print(f"el valor debe ser menor o igual a {maximo}")
            else:
                validado = True
        except:
            print('no es un numero valido intentelo nuevamente')
    
    return n

def inputNumber(tipoDato, mensaje, x=None, y=None, maximo=None, minimo=None):
    validado = False
    
    while not validado:
        try:
            n = tipoDato(input(mensaje+" "))
            
            if x is not None and y is not None:
                if n >= x and n <= y:
                    validado = True
                else:
                    print(f"el valor debe estar entre {x} y {y}")
            elif minimo is not None and n < minimo:
                print(f"el valor debe ser mayor o igual a {minimo}")
            elif maximo is not None and n > maximo:
                print(f"el valor debe ser menor o igual a {maximo}")
            else:
                validado = True
        except:
            print('no es un numero valido intentelo nuevamente')
    
    return n