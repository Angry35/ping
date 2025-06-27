from youtubesearchpython import VideosSearch


def buscar(keyword):
    videos = VideosSearch(keyword, limit =10)
    resultado = videos.result()["result"]
    listas=[video["title"] for video in resultado]
    return listas
keyword= "chimichanga"
listas = buscar(keyword)
for lista in listas:
    print(lista)
