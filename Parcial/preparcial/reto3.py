#3)	Escribe un programa que divida un texto largo en líneas de hasta 30 caracteres.

textoLargo = "Sed condimentum diam orci, eget condimentum ipsum convallis quis. Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipiscing velit, sed quia non numquam do eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur?"
textoForFor = textoLargo.split()
lineas = []
lineaActual = ""

for palabra in textoForFor:
    if len(lineaActual) + len(palabra) <= 30:
        lineaActual += palabra + " "
    else:
        lineas.append(lineaActual)
        lineaActual = palabra + " "

for linea in lineas:
    print(linea)