import sys
import os.path
import cv2
from matplotlib import pyplot as plt

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

# calcular descriptores (histogramas)

images_folder = os.listdir(dataset_r)
dict_images = {}

# # primero se itera en la carpeta que contiene las imagenes originales
for image_path in images_folder:
    # se lee la imagen es escala de grises
    img = cv2.imread(dataset_r + image_path, cv2.IMREAD_GRAYSCALE) # or just 0
    height, width = img.shape # se obtienen las dimensiones de la imagen

    # # se procede a calcular 4
    imgs = [0]*4
    hist = [0]*4
    for i in range(4):
        imgs[i] = img[(height//4)*i:(height//4)*(i+1),:]

    for i in range(4):
        hist[i] = cv2.calcHist(imgs[i], [0], None, [4], [0,256]) # 32 - 64
        

    dict_images[image_path] = hist




    
    
    
 


