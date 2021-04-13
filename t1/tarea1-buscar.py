import sys
import os.path
import cv2
import numpy as np
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
fichero = open("datos_R/dict_images_r", "rb")
dict_images_r = pickle.load(fichero) # se cargan los datos

dict_images_q = {}

# Procesamiento de las imagenes de consulta
for image_path in os.listdir(dataset_q):
    img = cv2.imread(dataset_q + image_path, cv2.IMREAD_GRAYSCALE) # or just 0
    # se obtienen las dimensiones de la imagen
    height, width = img.shape
    '''
        Para calcular los descriptores de las imagenes de Q se hace
        lo mismo que se hizo en el procesamiento de las imagenes de R
        en tarea1-procesar.py
    '''
    imgs = [0]*5
    hist = np.empty(0, dtype="float32")
    for i in range(5):
        imgs[i] = img[(height//5)*i:(height//5)*(i+1),:]
        h = cv2.calcHist(imgs[i], [0], None, [64], [0,256])
        hist = np.append(hist,h)
    dict_images_q[image_path] = hist

'''
    Una vez que se calculan los descriptores de las imagenes de Q se procede a realizar la busqueda
'''
# Busqueda

lista_resultados = [] # lista que almacenara los resultados
for k1 in dict_images_q:
    h1 = dict_images_q[k1]
    '''
        Diccionario que almacenara las distancias de las imagenes reales con respecto a a la imagen de consulta
    '''
    D = {}
    for k2 in dict_images_r:
        h2 = dict_images_r[k2]
        '''
            Metodos de comparacion: 
            - HISTCMP_CHISQR (53%-52%-54% -> ~5)
            - HISTCMP_BHATTACHARYYA (65%-64%-65% -> ~6)
            - HISTCMP_CHISQR_ALT (67%-67%-68% -> ~6.3)

            Se decide usar el método de CHISQR_ALT ya que fue 
            el que mejores resultados obtuvo.
        '''
        dist = cv2.compareHist(h1,h2, cv2.HISTCMP_CHISQR_ALT)
        D[k2] = dist
    min_key = min(D, key=D.get) # Llave del valor minimo del dict
    lista_resultados.append([k1, min_key, D[min_key]])

# Escribir en resultados

# Se crea el archivo que contendrá los resultados
res = open(resultados, "w+")

for i in range(len(lista_resultados)):
    img1, img2, dist = lista_resultados[i]
    res.write(f"{img1} \t {img2} \t {dist}\n")