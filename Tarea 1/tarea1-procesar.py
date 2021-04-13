import sys
import os.path
import cv2
import numpy as np
import pickle

if len(sys.argv) < 2:
    print("Uso: {} [dataset_r] [datos]".format(sys.argv[0]))
    sys.exit(1)

dataset_r = sys.argv[1]
datos = sys.argv[2]


if not os.path.isdir(dataset_r):
    print("no existe directorio {}".format(dataset_r))
    sys.exit(1)

if not os.path.isdir(datos):
    print("creando directorio {}".format(datos))
    os.mkdir(datos)

# Diccionario que almacenara los descriptores de las imagenes de R
dict_images_r = {}

# Procesamiento de las imagenes reales R
for image_path in os.listdir(dataset_r):
    img = cv2.imread(dataset_r + image_path, cv2.IMREAD_GRAYSCALE) # or just 0
    # se obtienen las dimensiones de la imagen
    height, width = img.shape
    '''
        Se divide horizontalmente la imagen original en 5 imagenes. A cada
        una de estas imagenes se le calcula su respectivo histograma para luego
        agregar al diccionario el path de la imagen con su respectivo vector
        de histogramas.
    '''
    imgs = [0]*5
    hist = np.empty(0, dtype="float32")
    for i in range(5):
        imgs[i] = img[(height//5)*i:(height//5)*(i+1),:]
        h = cv2.calcHist(imgs[i], [0], None, [64], [0,256])
        hist = np.append(hist,h)
    dict_images_r[image_path] = hist

'''
    Ahora que se tiene el dict con las imagenes y sus descriptores,
    se procede a codificar el dict en un archivo binario externo
    para poder utilizar su contenido en el archivo de busqueda.
    Para llevar a cabo esto se utiliza la libreria *pickle*.
'''
fichero_binario = open("datos_R/dict_images_r", "wb") # se crea el fichero
# Se "vuelca" la informacion del diccionario en el fichero
pickle.dump(dict_images_r, fichero_binario)

fichero_binario.close() # Cerramos el fichero