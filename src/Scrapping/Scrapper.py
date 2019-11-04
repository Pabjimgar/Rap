import requests
from bs4 import BeautifulSoup
import logging

estilo = "line-height:22px;font-size:16px;font-family:arial,tahoma,verdana"
tipo_de_archivo = ".txt"
empty_string = ""
div_class = "lyrics-body"

logging.basicConfig(level=logging.INFO)


def get_urls_from_songs_file(direction):

    """Función diseñada para parsear un fichero con urls de un artista y devolver una lista con las mismas"""
    logging.info("ABRIENDO ARCHIVO PARA CONSEGUIR URL")
    with open(direction, "r") as song_list_file:
        reader = song_list_file.read()
        return [str(song) for song in reader.split("\n")]


def get_soup_from_url(url):

    """Con esta función podemos devolver la sopa parseada en html"""

    request_de_la_cancion = requests.get(url)
    html_de_la_cancion = request_de_la_cancion.text
    return BeautifulSoup(html_de_la_cancion, "html.parser")


def get_text_from_url(nombre_del_cantante, url):

    """Esta función toma como input el nombre del cantante y la url de una de sus canciones
    con el propósito de obtener una sopa en BeautifulSoup, para llamar a save_to_file"""

    sopa_de_la_cancion = get_soup_from_url(url)
    texto_de_la_sopa = sopa_de_la_cancion.find("div", id="letra")\

    for tag in texto_de_la_sopa:
        return save_to_file(nombre_del_cantante, tag.text)


def clean_text_of_soup(nombre_del_cantante, text_of_soup):

    """Función para tomar el texto de una canción y eliminar aquellas palabras y espacios en blanco
    que no forman parte de la letra"""

    text_without_header = text_of_soup.split(nombre_del_cantante, 1)[1]
    return text_without_header.split("Agregar a la playlist")[0].rstrip()


def save_to_file(nombre_del_cantante, texto_de_la_cancion):

    """ Esta función toma tanto el nombre del cantante, como el texto de una sopa y la guarda en un archivo,
    del que cuenta las palabras, y las devuelve para el contador """

    with open(nombre_del_cantante + tipo_de_archivo, "a") as text_file:

        text_file.write(texto_de_la_cancion)
        text_file.write("\n")

    # TODO Futuro método para poder contar número de palabras
    # with open(nombre_del_cantante + tipo_de_archivo, "r") as text_file:
    #
    #     total_words = [word for line in text_file for word in line.split()]
    #     return total_words


def get_text_from_letras_com_soup(nombre_del_cantante, url):

    """Función para guardar las letras de un artista en un archivo"""

    soup = get_soup_from_url(url)
    text_of_soup = soup.find("article").get_text(" ")
    text_without_header = clean_text_of_soup(nombre_del_cantante, text_of_soup).lstrip()

    return save_to_file(nombre_del_cantante, text_without_header)

    




