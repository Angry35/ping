import os
import subprocess
import re
import sys

carpeta = '/home/buddha/Vídeos/Grabaciones de la pantalla'

def obtener_duracion(video):
    comando = [
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        video
    ]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    salida = resultado.stdout.strip()
    if salida == '':
        raise ValueError(f"No se pudo obtener duración del video: {video}")
    return float(salida)

def convertir_con_barra(ruta_entrada, ruta_salida):
    duracion = obtener_duracion(ruta_entrada)

    comando = [
        'ffmpeg',
        '-i', ruta_entrada,
        '-c:v', 'libx264',
        '-crf', '23',
        '-preset', 'fast',
        '-c:a', 'aac',
        '-b:a', '128k',
        ruta_salida,
        '-y'  
    ]

    proceso = subprocess.Popen(comando, stderr=subprocess.PIPE, text=True)

    patron = re.compile(r'time=(\d+):(\d+):(\d+\.\d+)')

    while True:
        linea = proceso.stderr.readline()
        if not linea:
            break

        resultado = patron.search(linea)
        if resultado:
            h, m, s = resultado.groups()
            tiempo_actual = int(h) * 3600 + int(m) * 60 + float(s)
            porcentaje = (tiempo_actual / duracion) * 100
            sys.stdout.write(f"\rConvirtiendo... {porcentaje:.2f}%")
            sys.stdout.flush()

    proceso.wait()
    sys.stdout.write("\rConvirtiendo... 100.00%\n")

for archivo in os.listdir(carpeta):
    if archivo.endswith('.webm'):
        ruta_entrada = os.path.join(carpeta, archivo)
        nombre_sin_extension = os.path.splitext(archivo)[0]
        ruta_salida = os.path.join(carpeta, f"{nombre_sin_extension}.mp4")

        print(f"Procesando: {archivo}")
        try:
            convertir_con_barra(ruta_entrada, ruta_salida)
            os.remove(ruta_entrada)
            print(f" Convertido y eliminado: {archivo}")
        except Exception as e:
            print(f" Error al convertir {archivo}: {e}")
