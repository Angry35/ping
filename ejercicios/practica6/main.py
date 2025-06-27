#!/usr/bin/env python3
import os 
import shutil

while (True):

    if os.path.exists("Documentos") == True:
        pass
    else:
        os.mkdir("Documentos")
        continue
    if os.path.exists("Fotos") == True:
        pass
    else:
        os.mkdir("Fotos")
        continue
    if os.path.exists("Videos") == True:
        pass
    else:
        os.mkdir("Videos")
        continue
    if os.path.exists("Otros") == True:
        pass
    else:
        os.mkdir("Otros")
        continue
    if os.path.exists("Musica") == True:
        pass
    else:
        os.mkdir("Musica")
        continue
    break

ext_documentos= ".pdf", ".docx", ".txt", ".odt",".ppt", ".pttx"
documentos = [_ for _ in os.listdir() if _.endswith(ext_documentos)]

for i in documentos:
    if os.path.exists(i):
        shutil.move (i,"Documentos")

ext_fotos= ".jpg", ".png", ".jpeg", ".gif",".webp", ".bmp", ".ai", ".svg", "eps"
fotos = [_ for _ in os.listdir() if _.endswith(ext_fotos)]

for i in fotos:
    if os.path.exists(i):
        shutil.move (i,"Fotos")

ext_musica= ".wav", ".aiff", ".dsd", ".pcm",".flac", ".mp3"
musica = [_ for _ in os.listdir() if _.endswith(ext_musica)]

for i in musica:
    if os.path.exists(i):
        shutil.move (i,"Musica")

ext_videos= ".mp4", ".mov", ".avi", ".mkv",".avi", ".flv"
videos = [_ for _ in os.listdir() if _.endswith(ext_videos)]

for i in videos:
    if os.path.exists(i):
        shutil.move (i,"Videos")

ext_otros= ".ova", ".zip", ".rar", ".html",".psd", ".deb", ".ymp", ".exe", ".part", "tar.gz", ".flatpakref", ".desktop", "ovl", ".edn", ".jpl" ,"AppImage"
otros = [_ for _ in os.listdir() if _.endswith(ext_otros)]

for i in otros:
    if os.path.exists(i):
        shutil.move (i,"Otros")
