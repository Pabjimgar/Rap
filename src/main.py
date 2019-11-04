from Scrapping import MongoWriter, Scrapper
from Visualization import WordCloud, MongoReader
import sys
import logging

if __name__ == '__main__':

    # 1. PASAMOS EL NOMBRE DEL CANTANTE Y EL ARCHIVO CORRESPONDIENTE PARA CONSEGUIR UN FICHERO CON LA LETRA DE LAS
    #    CANCIONES DE LOS DOS PRIMEROS ÁLBUMES.
    logging.basicConfig(level=logging.INFO)
    # logging(str(sys.thread_info))

    cantante = sys.argv[1]
    lista_url_de_canciones = Scrapper.get_urls_from_songs_file(sys.argv[1] + "_canciones.txt")
    estilo = sys.argv[2]
    pais = sys.argv[3]

    logging.info("cantante: " + sys.argv[1])
    logging.info("estilo: " + cantante)
    logging.info("pais: " + cantante)

    # 2. POR CADA CANCION GENERAMOS UNA LÍNEA EN EL FICHERO DE SALIDA
    for cancion in lista_url_de_canciones:
        counter_por_cancion = Scrapper.get_text_from_letras_com_soup(cantante, cancion)

    # 3. ESCRIBIMOS LOS RESULTADOS EN MONGO, DENTRO DE LA COLECCIÓN artists_raw
    MongoWriter.file_to_mongo(cantante + ".txt", cantante, estilo, pais)

    stats = MongoReader.read_from_mongo(cantante)

    WordCloud.show_wordcloud(stats)
