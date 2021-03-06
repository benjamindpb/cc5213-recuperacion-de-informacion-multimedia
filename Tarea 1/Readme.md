# Tarea 1: Buscador de imagenes derivadas o duplicadas

## Procesamiento
 Para ser robustos a *flip* cada imagen original se dividio horizontalmente en 5 zonas a las cuales se les calculó individualmente sus respectivos **histogramas de intensidades**. Estos histogramas fueron calculados usando la función **calcHist** de la libreria **opencv**. Con esto se obtiene un vector de histogramas que va a servir para hacer la busqueda de las imagenes de query. Se consideró usar un diccionario tal que la llave corresponde al nombre de la imagen y el valor es el vector de histogramas.

 La información de cada imagen fue guardada en un **archivo binario externo** usando la libreria **pickle**. 

## Busqueda
Se calculan los descriptores de cada imagen de consulta de manera analoga al paso anterior.
Para realizar la busqueda se itera sobre el diccionario de imagenes de consulta, y para cada imagen se itera sobre el diccionario de las imagenes reales que se obtiene al leer el archivo binario antes creado. Luego se procede a comparar los histogramas de cada imagen usando la funcion **compareHist** de la libreria **opencv**. Los valores son guardados en otro diccionario, del cual una vez terminada la iteración de las imagenes reales se obtiene la menor distancia junto con su llave correspondiente. Cabe destacar que para realizar la comparación se utilizó el método de comparacion **cv2.HISTCMP_CHISQR_ALT** que fue el que entregó mejores resultados. Posteriormente una vez que se obtienen las imagenes y las distancias, se agregan a una lista para finalmente guardar toda la informacion en un archivo de texto donde se encuentran los resultados de la busqueda.

## Librerias utilizadas
opencv, numpy, pickle

## Forma de compilación
Esta tarea utiliza Python 3.8.3 y opencv 4.5.1.48.

Para evaluar la tarea se debe ejecutar el siguiente comando:
```console
python tarea1-test.py 
```

## Resultados Obtenidos
Para los tres dataset los resultados fueron bastante similares. Los puntos más altos de la busqueda fueron para los tipos de query **Q-QUALITY** y obviamente **F-FLIP**, obteniendo casi el 100% de aciertos. En cambio el tipo de query que obtuvo la puntuación más baja fue **G-GAMMA**. En general se obtuvo un logro de un 70% de aciertos en la busqueda de imagenes.