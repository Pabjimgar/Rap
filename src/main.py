from Scrapping import Scrapper
from Visualization import StyleVisualization, ArtistVisualization
from Preprocessing import Style_processing, Database_ops
from bson.objectid import ObjectId
import sys
import logging
import os.path
import pandas as pd

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
        checkpoint = str(input("Datos del cantante o del estilo?"))

        if checkpoint == "cantante":

            loggeo_principio_proceso(accion, cantante, estilo)
            lista_url_de_canciones = Scrapper.get_urls_from_songs_file(Scrapper.PATH_ARCHIVO_CANCIONES + estilo + "/" +
                                                                       cantante + "_canciones.txt")

            path_destino = Scrapper.PATH_LETRA_CANCIONES + estilo + "/" + cantante + Scrapper.TIPO_ARCHIVO
            if os.path.exists(path_destino):
                logging.info("Este archivo de letras ya existe")
                logging.info("Insertando letras de %s.txt" % cantante)
            else:
                for cancion in lista_url_de_canciones:
                    counter_por_cancion = Scrapper.get_text_from_letras_com_soup(cantante, cancion)

            Database_ops\
                .file_to_mongo(Scrapper.PATH_LETRA_CANCIONES + estilo + "/" + cantante + ".txt", cantante, estilo)

        elif checkpoint == "estilo":
            docs = Database_ops.set_style_collection(estilo)
            Style_processing.consolidate_style(docs, estilo, "test")

    elif accion.lower() == "leer":
        checkpoint = str(input("Datos del cantante o del estilo?"))

        if checkpoint.lower() == "cantante":
            loggeo_principio_proceso(accion, cantante, estilo)
            stats = Database_ops.read_artist_from_mongo(estilo, cantante, "text_no_sw")
            ArtistVisualization.show_freqdist(stats)

        elif checkpoint.lower() == "grupos":
            loggeo_principio_proceso(accion, "None", estilo)

            stats = Database_ops.set_style_collection(estilo).find()
            data = pd.DataFrame(list(stats))
            # todo crear visualizaciones por estilo a partir del DF
            StyleVisualization.compare_artists(data, estilo)

        elif checkpoint.lower() == "estilo":
            # Creamos un dataframe de pandas vacio para añadir rows con la info de cada estilo
            lista_estilos = ["Flamenco", "Indie"]
            columnas = ["_id","text_no_sw","unique_words","number_of_songs","word_average_per_song","max_words_per_song","min_words_per_song"]

            df_vacio= pd.DataFrame(columns=columnas, index=lista_estilos)

            for genero in lista_estilos:

                stats = Database_ops.set_style_collection(genero).find()
                data = pd.DataFrame(list(stats))

                data_genero = data[data["_id"] == genero]
                columnas_data_genero = list(data_genero.values)
                df_vacio.loc[genero] = columnas_data_genero

            print(df_vacio.head())

    else:
        logging.error("Acción no comtemplada")
