#Determinar cuál es la vocal que aparece con mayor frecuencia.

frase = "Quiero comer manzanas, solamente manzanas."
ca = 0
ce = 0
ci = 0
co = 0
cu = 0
for letra in frase:
    if letra == "a":
        ca += 1
    elif letra == "e":
        ce += 1
    elif letra == "i":
        ci += 1
    elif letra == "o":
        co += 1
    elif letra == "u":
        cu += 1

if ca > ce and ca > ci and ca > co and ca > cu:
    print("la vocal que mas aparece es la a: ",ca," veces")
if ce > ca and ce > ci and ce > co and ce > cu:
    print("la vocal que mas aparece es la e: ",ce," veces")
if ci > ce and ci > ca and ci > co and ci > cu:
    print("la vocal que mas aparece es la i: ",ci," veces")
if co > ce and co > ci and co > ca and co > cu:
    print("la vocal que mas aparece es la o: ",co," veces")
if cu > ce and cu > ci and cu > co and cu > ca:
    print("la vocal que mas aparece es la u: ",cu," veces")