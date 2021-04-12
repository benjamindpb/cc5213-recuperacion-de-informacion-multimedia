import sys
import os.path
import cv2
from matplotlib import pyplot as plt
import pickle

if len(sys.argv) < 3:
    print("Uso: {} [dataset_q] [datos] [resultados]".format(sys.argv[0]))
    sys.exit(1)

dataset_q = sys.argv[1]
datos = sys.argv[2]
resultados = sys.argv[3]

if not os.path.isdir(dataset_q):
    print("no existe directorio {}".format(dataset_q))
    sys.exit(1)

if not os.path.isdir(datos):
    print("no existe directorio {}".format(datos))
    sys.exit(1)

'''
    Se abre el fichero binario que fue calculado en el procesamiento
    de las imagenes para utilizar su informacion.
'''
fichero = open("datos_R/dict_images", "rb")
dict_images_r = pickle.load(fichero) # se cargan los datos

dict_images_q = {}

for image_path in os.listdir(dataset_q):
    img = cv2.imread(dataset_q + image_path, cv2.IMREAD_GRAYSCALE) # or just 0
    # se obtienen las dimensiones de la imagen
    height, width = img.shape
    '''
        Para calcular los descriptores de las imagenes de Q se hace
        lo mismo que se hizo en el procesamiento de las imagenes de R
    '''
    imgs = [0]*4
    hist = [0]*4
    for i in range(4):
        imgs[i] = img[(height//4)*i:(height//4)*(i+1),:]
    for i in range(4):
        hist[i] = cv2.calcHist(imgs[i], [0], None, [64], [0,256]) # 32 - 64
    dict_images_q[image_path] = hist

for key in dict_images_q:
    print(cv2.compareHist(dict_images_q[key][1],dict_images_q[key][3],cv2.HISTCMP_CHISQR)) # 1 
    break

# escribir en resultados

'''
    Lo que hice fue dividir la imagen horizontalmente en 4 imagenes. Luego 
    para cada imagen calcule su histograma. Es decir a cada imagen le corresponde un ARRAY
    de 4 histogramas. ¿Como los comparo ahora con los 4 histogramas de las imagenes en Q? 
    ¿Como puedo determinar solo UNA distancia si tengo 4? ¿Hago un promedio? ¿Las sumo? D:
'''