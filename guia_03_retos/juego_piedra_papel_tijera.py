### agregar contador indivual al ganar o perder e ir mostrandolo a medida que van jugando


from random import choice
contadorDeUsuario = 0
contadorDelBot = 0
terminadorDeJuego = 1
while terminadorDeJuego != 0:


    
    eleccionUsuario = input("Piedra, Papel o Tijera?\n")
    computerChoice = choice(['piedra', 'papel', 'tijera'])


    if eleccionUsuario == computerChoice:
        print("Empate, elegieron lo mismo")
    elif eleccionUsuario == "piedra":
        if computerChoice == "papel":
            print("Perdiste!! la computadora elegio papel")
            contadorDelBot = contadorDelBot + 1
        else:
            print("Ganaste!! la computadora elegio tijera")
            contadorDeUsuario = contadorDeUsuario + 1
    elif eleccionUsuario == "papel":
        if computerChoice == "piedra":
            print("Ganaste!!, la computadora eligio piedra")
            contadorDeUsuario = contadorDeUsuario + 1
        else:
            print("Perdiste, la computadora elegio tijeras")
            contadorDelBot = contadorDelBot + 1
    elif eleccionUsuario == "tijera":
        if computerChoice == "papel":
            print("ganaste, la computadora eligio papel")
            contadorDeUsuario = contadorDeUsuario + 1
        else:
            print("perdiste, la computadora eligio piedra ")
            contadorDelBot = contadorDelBot + 1
    if contadorDelBot == 3:
        print("Gano la maquina, ojo con skynet")
        terminadorDeJuego = 0
    if contadorDeUsuario == 3:
        print("ganaste que afortunado")
        terminadorDeJuego = 0

