# /usr/bin/python3.7
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

img1 = cv2.imread(dataset_r + os.listdir(dataset_r)[542], cv2.IMREAD_GRAYSCALE) # or just 0

print(img1.shape)

cv2.imshow(os.listdir(dataset_r)[542], img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
# img2 = cv2.imread(dataset_r + os.listdir(dataset_r)[67], cv2.IMREAD_GRAYSCALE) # or just 0

# hist1 = cv2.calcHist(img1, [0], None, [32], [0,256])
# hist2 = cv2.calcHist(img2, [0], None, [32], [0,256])
# print(cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR))

# images_folder = os.listdir(dataset_r)

# # primero se itera en la carpeta que contiene las imagenes originales
# for image_path in images_folder:
#     # se lee la imagen
#     img = cv2.imread(dataset_r + image_path, cv2.IMREAD_GRAYSCALE) # or just 0
    
#     hist = cv2.calcHist(img, [0], None, [32], [0,256])

    
    
    
 


