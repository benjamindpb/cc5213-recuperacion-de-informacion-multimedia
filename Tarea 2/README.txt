CC5213 - RECUPERACIÓN DE INFORMACIÓN MULTIMEDIA
Profesor: Juan Manuel Barrios
Fecha: 13 de abril de 2021


1. Descargar todos los archivos de esta carpeta.

2. Para verificar que ha descargado bien y que tiene el mismo archivo escribir el comando:
		md5sum -c MD5SUM

  Para Windows existen múltiples implementacionesde md5sum. El port de la versión de GNU se
  puede descargar desde: http://gnuwin32.sourceforge.net/packages/coreutils.htm

3. Leer el enunciado de la tarea.

4. Para resolver la tarea debe escribir cuatro programas:

	1) tarea2-extractor-audio.py
	2) tarea2-extractor-visual.py
	3) tarea2-busqueda.py
	4) tarea2-deteccion.py

 Se incluye una base para estos cuatro archivos. En el enunciado se describe lo que debe hacer cada uno.

5. Para evaluar su tarea debe ejecutar el comando:

	python tarea2-ejecutar.py

Ese comando evalúa su atrea en los tres datasets disponibles.
En la consola entregará la cantidad de respuestas correctas e incorrectas al comparar sus respuestas con los archivos gt.txt de cada dataset.
