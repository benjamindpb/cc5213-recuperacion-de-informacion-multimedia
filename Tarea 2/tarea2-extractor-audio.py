import sys
import os.path

if len(sys.argv) < 3:
    print("Uso: {} [carpeta_entrada] [carpeta_salida]".format(sys.argv[0]))
    sys.exit(1)

carpeta_entrada = sys.argv[1]
carpeta_salida = sys.argv[2]

if not os.path.isdir(carpeta_entrada):
    print("no existe directorio {}".format(carpeta_entrada))
    sys.exit(1)

#procesar todos los archivos de carpeta_entrada que terminen en (mp4 avi mpg wav mp3)
#para cada archivo:
#  extraer la pista de audio
#  dividir el audio en N segmentos de tiempo
#  calcular una matriz de descriptores de N filas por d columnas (d=dimension del descriptor)
#  crear directorio: os.mkdir(carpeta_salida)
#  escribir matriz descriptores en carpeta_salida/archivo
