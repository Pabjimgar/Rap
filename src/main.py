from Scrapping import MongoWriter, Scrapper
from Visualization import WordCloud, MongoReader
import sys
import logging
import os.path

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    accion = str(input("Quieres escribir o leer?"))
    cantante = sys.argv[1]
    estilo = sys.argv[2]

    def loggeo_principio_proceso(accion, cantante, estilo):
        logging.info("accion: " + accion)
        logging.info("cantante: " + cantante)
        logging.info("estilo: " + estilo)

    if accion.lower() == "escribir":
        loggeo_principio_proceso(accion, cantante, estilo)
        lista_url_de_canciones = Scrapper.get_urls_from_songs_file(Scrapper.PATH_ARCHIVO_CANCIONES + estilo + "/" + cantante + "_canciones.txt")

        path_destino = Scrapper.PATH_LETRA_CANCIONES + estilo + "/" + cantante + Scrapper.TIPO_ARCHIVO
        if os.path.exists(path_destino):
            logging.info("Este archivo de letras ya existe")
            logging.info("Insertando letras de %s.txt" % cantante)
        else:
            for cancion in lista_url_de_canciones:
                counter_por_cancion = Scrapper.get_text_from_letras_com_soup(cantante, cancion)

        MongoWriter.file_to_mongo(Scrapper.PATH_LETRA_CANCIONES + estilo + "/" + cantante + ".txt", cantante, estilo)

    elif accion.lower() == "leer":
        loggeo_principio_proceso(accion, cantante, estilo)
        stats = MongoReader.read_from_mongo(estilo, cantante, "text_no_sw")
        WordCloud.show_wordcloud(stats)

    else:
        logging.error("Acción no comtemplada")
