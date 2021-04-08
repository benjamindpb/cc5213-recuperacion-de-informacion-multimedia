# /usr/bin/python3.7
import sys
import os.path
import cv2

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

# calcular descriptores
print(dataset_r + os.listdir(dataset_r)[0]) # dataset_a/imagenes_q/a0963.jpg
img = cv2.imread(dataset_r + os.listdir(dataset_r)[0], cv2.IMREAD_GRAYSCALE) # or just 0

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# primero se itera en la carpeta que contiene las imagenes originales
for image_path in os.listdir(dataset_r):
    pass
    
 


