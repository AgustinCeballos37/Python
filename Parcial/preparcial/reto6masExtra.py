import argparse
import os

def eliminarComentarios(archivoEntrada, archivoSalida):
    with open(archivoEntrada, "r") as file:
        codigo = file.readlines()

    codigoLimpio = []

    for linea in codigo:
        if not linea[0] == "#":
            if not linea[0] == '"""':
                codigoLimpio.append(linea)

    carpetaActual = os.getcwd()
    rutaSalida = os.path.join(carpetaActual, archivoSalida)

    with open(rutaSalida, "w") as file:
        file.writelines(codigoLimpio)

parser = argparse.ArgumentParser(description="Eliminar comentarios de un archivo .py")
parser.add_argument("archivoEntrada", help="Archivo .py de entrada")
parser.add_argument("archivoSalida", help="Nombre del archivo .py de salida")

args = parser.parse_args()

eliminarComentarios(args.archivoEntrada, args.archivoSalida)