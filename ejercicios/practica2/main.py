import requests 

sitios = [
 
    "https://www.amazon.com",
    "https://www.google.com,"
    "https://www.instagram,com",
    "https://www.sourceforge.net",
    "https://www.facebook.com",
    "https://archive.org/",
    "https://www.pdfdrive.to/",
    "https://www.pdfdrive.to/",
    "http://www.beeweb.co/",
    "https://www.linkedin.com",
    "https://www.microsoft.com"
]

for sitio in sitios:
    try:
        respuesta= requests.head(sitio)
        print(f"{sitio}: {respuesta.status_code}")
    except requests.exceptions.RequestException as e:
        print (f"{sitio}: Error -{e}")
