import sys
import os.path
import subprocess

def run_command(comando):
    print()
    print("INICIANDO: {}".format(" ".join(comando)))
    code = subprocess.call(comando)
    if code != 0:
        print("ERROR!")
        sys.exit()


def evaluar_resultados(file_gt, file_detecciones_audio, file_detecciones_visual):
    comando = ["python", "tarea2-evaluar.py", file_gt, file_detecciones_audio, file_detecciones_visual]
    run_command(comando)

def ejecutar_comandos(dataset_dir, tipo):
    #ruta del dataset
    videos_comerciales = "{}/comerciales".format(dataset_dir)
    videos_television = "{}/television".format(dataset_dir)
    
    #validar las rutas del dataset
    if not os.path.isdir(videos_comerciales) or not os.path.isdir(videos_television):
        print("ruta {} no contiene un dataset".format(dataset_dir))
        return None
    
    #carpetas y archivo a crear durante la ejecución
    descriptores_television = "temp_{}_{}_tv".format(dataset_dir, tipo)
    descriptores_comerciales = "temp_{}_{}_com".format(dataset_dir, tipo)
    similares = "temp_{}_{}_similares".format(dataset_dir, tipo)
    file_detecciones = "temp_{}_{}_detecciones.txt".format(dataset_dir, tipo)
    
    #comandos a ejecutar
    comandos = []
    
    # tareas en python
    cmd_extractor = "tarea2-extractor-{}.py".format(tipo)
    cmd_busqueda = "tarea2-busqueda.py"
    cmd_deteccion = "tarea2-deteccion.py"
    comandos.append(["python", cmd_extractor, videos_television, descriptores_television])
    comandos.append(["python", cmd_extractor, videos_comerciales, descriptores_comerciales])
    comandos.append(["python", cmd_busqueda, descriptores_television, descriptores_comerciales, similares])
    comandos.append(["python", cmd_deteccion, similares, file_detecciones])
    
    # tareas en c++
    #cmd_extractor = "./tarea2-extractor-{}".format(tipo)
    #cmd_busqueda = "./tarea2-busqueda"
    #cmd_deteccion = "./tarea2-deteccion"
    #comandos.append([cmd_extractor, videos_television, descriptores_television])
    #comandos.append([cmd_extractor, videos_comerciales, descriptores_comerciales])
    #comandos.append([cmd_busqueda, descriptores_television, descriptores_comerciales, similares])
    #comandos.append([cmd_deteccion, similares, file_detecciones])
    
    # tareas en java
    #cmd_extractor = "tarea2-extractor-{}".format(tipo)
    #cmd_busqueda = "tarea2-busqueda"
    #cmd_deteccion = "tarea2-deteccion"
    #comandos.append(["java", cmd_extractor, videos_television, descriptores_television])
    #comandos.append(["java", cmd_extractor, videos_comerciales, descriptores_comerciales])
    #comandos.append(["java", cmd_busqueda, descriptores_television, descriptores_comerciales, similares])
    #comandos.append(["java", cmd_deteccion, similares, file_detecciones])

    # ejecutar todos los comandois
    for comando in comandos:
        run_command(comando)

    # retonar el archivo con las detecciones
    return file_detecciones


# inicio
print("CC5213 - EJECUTANDO TAREA 2 (2021-1)")

datasets = ["dataset_a", "dataset_b", "dataset_c"]

for dataset_dir in datasets:
    file_detecciones_audio = ejecutar_comandos(dataset_dir, "audio")
    file_detecciones_visual = ejecutar_comandos(dataset_dir, "visual")
    file_gt = "{}/gt.txt".format(dataset_dir)
    evaluar_resultados(file_gt, file_detecciones_audio, file_detecciones_visual)
