import sys
import os.path
import subprocess
import librosa

if len(sys.argv) < 3:
    print("Uso: {} [carpeta_entrada] [carpeta_salida]".format(sys.argv[0]))
    sys.exit(1)

carpeta_entrada = sys.argv[1]
carpeta_salida = sys.argv[2]

if not os.path.isdir(carpeta_entrada):
    print("no existe directorio {}".format(carpeta_entrada))
    sys.exit(1)

# se crea la carpeta de los datos de las pistas de audio
if not os.path.isdir(carpeta_salida):
    print("creando directorio {}".format(carpeta_salida))
    os.mkdir(carpeta_salida)

#procesar todos los archivos de carpeta_entrada que terminen en (mp4 avi mpg wav mp3)
#para cada archivo:
#  extraer la pista de audio
#  dividir el audio en N segmentos de tiempo
#  calcular una matriz de descriptores de N filas por d columnas (d=dimension del descriptor)
#  crear directorio: os.mkdir(carpeta_salida)
#  escribir matriz descriptores en carpeta_salida/archivo

sample_rate = 8192 # cada segundo hay 44100 samples

L = []

for file_path in os.listdir(carpeta_entrada):
    # # nombre que se le da al audio
    # file_wav = "{}.wav".format(file_path)
    # # este comando se encarga de extraer la pista de audio
    # comando = ["ffmpeg", "-i", carpeta_entrada + "/" + file_path, "-ac", "1", "-ar", str(sample_rate), carpeta_salida + "/" + file_wav]
    # # la siguiente linea genera un nuevo proceso que ejecuta el comando para 
    # # extraer la pista de audio
    # code = subprocess.call(comando)
    # if code != 0:
    #     raise Exception("ERROR!")

    """
        Ahora se debe dividir el audio en segmentos de largo fijo y calcular
        un único vector por segmento, luego se juntan (?)

        MFCC (?)
    """

    ventana = 256
    salto = 256
    dimension = 32

    path_file_wav = carpeta_salida + "/dove desodorante hombre.mp4.wav"
    y, sr = librosa.load(path_file_wav, sample_rate)
    print(len(y))
    print(sr)
    mfcc = librosa.feature.mfcc(y, sr=sr, n_mfcc=dimension, n_fft=ventana, hop_length=salto)
    print(mfcc.transpose().shape)
    break