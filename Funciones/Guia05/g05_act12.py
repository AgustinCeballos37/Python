def cargaUsuario():
    nombreCompleto = input("Ingrese un nombre completo en la forma <nombre> <apellido>\n")
    return nombreCompleto

def inversionUsuario():
    nombreDevuelto = cargaUsuario()
    nombreEnLista = nombreDevuelto.split()
    nombreInvertido = nombreEnLista[1] + ", " + nombreEnLista[0]
    return nombreInvertido
print(inversionUsuario())