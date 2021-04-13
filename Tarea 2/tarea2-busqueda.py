import sys
import os.path

if len(sys.argv) < 4:
    print("Uso: {} [carpeta_descriptores_television] [carpeta_descriptores_comerciales] [carpeta_similares]".format(sys.argv[0]))
    sys.exit(1)

carpeta_descriptores_television = sys.argv[1]
carpeta_descriptores_comerciales = sys.argv[2]
carpeta_similares = sys.argv[3]

if not os.path.isdir(carpeta_descriptores_television):
    print("no existe directorio {}".format(carpeta_descriptores_television))
    sys.exit(0)

if not os.path.isdir(carpeta_descriptores_comerciales):
    print("no existe directorio {}".format(carpeta_descriptores_comerciales))
    sys.exit(0)

#cargar todos los descriptores en carpeta_descriptores_television (conjunto Q)
#cargar todos los descriptores en carpeta_descriptores_comerciales (conjunto R)
#para cada descriptor de q de Q encontrar el descriptor más cercano r de R
#escribir los pares más cercanos (q,r) en un archivo dentro de carpeta_similares
