import sys
import subprocess


def ejecutar(comando):
    print(comando)
    code = subprocess.call(comando)
    if code != 0:
        print("ERROR!")
        sys.exit()


def ejecutar_comandos(dataset_q, dataset_r, datos, resultados, filename_gt):
    # comandos para tareas python
    comando1 = ["python", "tarea1-procesar.py", dataset_r, datos]
    comando2 = ["python", "tarea1-buscar.py", dataset_q, datos, resultados]

    # comandos para tareas c++
    # comando1 = ["./tarea1-procesar", dataset_r, datos]
    # comando2 = ["./tarea1-buscar", dataset_q, datos, resultados]

    # comandos para tareas java
    # comando1 = ["java", "tarea1-procesar", dataset_r, datos]
    # comando2 = ["java", "tarea1-buscar", dataset_q, datos, resultados]

    # comando para evaluacion
    comando3 = ["python", "tarea1-evaluar.py", filename_gt, resultados]

    # ejecutar los comandos
    ejecutar(comando1)
    ejecutar(comando2)
    ejecutar(comando3)


def ejecutar_dataset(nombre):
    dataset_q = "{}/imagenes_q/".format(nombre)
    dataset_r = "{}/imagenes_r/".format(nombre)
    filename_gt = "{}/gt.txt".format(nombre)
    datos = "datos_{}".format(nombre)
    resultados = "resultados_{}.txt".format(nombre)
    ejecutar_comandos(dataset_q, dataset_r, datos, resultados, filename_gt)


print("CC5213 - Tarea 1  (2021-2)")
ejecutar_dataset("dataset_a")
ejecutar_dataset("dataset_b")
ejecutar_dataset("dataset_c")
