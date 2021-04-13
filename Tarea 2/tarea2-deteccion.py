import sys
import os.path

if len(sys.argv) < 3:
    print("Uso: {} [carpeta_similares] [archivo_detecciones]".format(sys.argv[0]))
    sys.exit(1)

carpeta_similares = sys.argv[1]
archivo_detecciones = sys.argv[2]

if not os.path.isdir(carpeta_similares):
    print("no existe carpeta {}".format(carpeta_similares))
    sys.exit(0)

#leer datos en carpeta_similares
#buscar secuencias de un mismo video con un mismo offset
#escribir los comerciales detectados en archivo_detecciones
