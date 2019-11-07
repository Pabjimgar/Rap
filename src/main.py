from Scrapping import MongoWriter, Scrapper
from Visualization import WordCloud, MongoReader
import sys
import logging

if __name__ == '__main__':

    # 1. PASAMOS EL NOMBRE DEL CANTANTE Y EL ARCHIVO CORRESPONDIENTE PARA CONSEGUIR UN FICHERO CON LA LETRA DE LAS
    #    CANCIONES DE LOS DOS PRIMEROS ÁLBUMES.
    logging.basicConfig(level=logging.INFO)
    # logging(str(sys.thread_info))

    #todo DISEÑAR SISTEMA PARA MODULAR EL MAIN MEJOR EN ACCIONES

    accion = str(input("Quieres escribir o leer?"))
    cantante = sys.argv[1]
    estilo = sys.argv[2]
    pais = sys.argv[3]

    def loggeo_principio_proceso(accion, cantante, estilo, pais):
        logging.info("accion: " + accion)
        logging.info("cantante: " + cantante)
        logging.info("estilo: " + estilo)
        logging.info("pais: " + pais)


    if accion.lower() == "escribir":
        loggeo_principio_proceso(accion, cantante, estilo, pais)
        lista_url_de_canciones = Scrapper.get_urls_from_songs_file(sys.argv[1] + "_canciones.txt")

        for cancion in lista_url_de_canciones:
            counter_por_cancion = Scrapper.get_text_from_letras_com_soup(cantante, cancion)

        MongoWriter.file_to_mongo(cantante + ".txt", cantante, estilo, pais)

    elif accion.lower() == "leer":
        loggeo_principio_proceso(accion, cantante, estilo, pais)
        stats = MongoReader.read_from_mongo(cantante, "text_raw")
        WordCloud.show_wordcloud(stats)

    else:
        logging.error("Acción no comtemplada")
