import sys
import logging
import os.path
from Scrapping import Scrapper
from Visualization import StyleVisualization, ArtistVisualization
from Preprocessing import Style_processing, Database_ops
from Preprocessing.Tags import DbTags
from Generator import Generator
import pandas as pd
import json

STYLES = "Styles"

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    accion = str(input("Quieres escribir o leer?"))
    cantante = sys.argv[1]
    estilo = sys.argv[2]

    with open("albums.json") as f:
        n_albums = json.load(f)[cantante]

    dbTags = DbTags

    def loggeo_principio_proceso(accion, cantante, estilo):
        logging.info("accion: " + accion)
        logging.info("cantante: " + cantante)
        logging.info("estilo: " + estilo)

    if accion.lower() == "escribir":
        checkpoint = str(input("Datos del cantante, del estilo o todo?"))

        if checkpoint == "cantante":

            loggeo_principio_proceso(accion, cantante, estilo)
            lista_url_de_canciones = Scrapper.get_urls_from_songs_file(Scrapper.PATH_ARCHIVO_CANCIONES+ estilo + "/" + cantante + "_canciones.txt")

            path_destino = Scrapper.PATH_LETRA_CANCIONES + estilo + "/" + cantante + Scrapper.TIPO_ARCHIVO
            if os.path.exists(path_destino):
                logging.info("Este archivo de letras ya existe")
                logging.info("Insertando letras de %s.txt" % cantante)
            else:
                for cancion in lista_url_de_canciones:
                    counter_por_cancion = Scrapper.get_text_from_letras_com_soup(cantante, cancion)

            Database_ops\
                .file_to_mongo(Scrapper.PATH_LETRA_CANCIONES + estilo + "/" + cantante + ".txt", cantante, estilo, n_albums)

        elif checkpoint == "estilo":
            docs = Database_ops.set_style_collection(estilo)
            Style_processing.consolidate_style(docs, estilo, STYLES)

        elif checkpoint == "todo":
            docs = Database_ops.set_style_collection(STYLES)
            Style_processing.consolidate_style(docs, STYLES, STYLES)

    elif accion.lower() == "leer":
        checkpoint = str(input("Datos del cantante, del estilo o proyecto?"))

        stats = Database_ops.set_style_collection(estilo).find()
        data = pd.DataFrame(list(stats))

        if checkpoint.lower() == "cantante":
            loggeo_principio_proceso(accion, cantante, estilo)

            # 1. Primera visualización: FreqDist

            statistics = Database_ops.read_artist_from_mongo(estilo, cantante, "text_no_sw")
            ArtistVisualization.show_freqdist(statistics)

            # Hay que cambiar stats para que pueda leer los datos completos y no tan solo las palabras, y con esos datos
            # alimentar un spider chart donde ver cada cantante
            #
            # clean_data = Spider_preprocessing.df_cleaning(data)
            #
            # data_spider = data[data["_id"] == cantante][[tags.id, tags.text_no_sw, tags.unique_words,
            #                                              tags.number_of_stopwords]]

            # ArtistVisualization.show_spider_graph(data_spider)

        elif checkpoint.lower() == "estilo":
            loggeo_principio_proceso(accion, "None", estilo)

            # 1. Primera visualización: WordCloud
            data_cloud = data[data[DbTags.id] == estilo][DbTags.text_no_sw].values
            StyleVisualization.show_wordcloud(data_cloud)

            # 2. Segunda visualización: Graficos comparativos
            data_no_cloud = data[data[DbTags.id] != estilo]
            StyleVisualization.compare_artists(data, estilo)

            # 3. Tercera visualización: Queso de discos
            n_albums_artistas = data[data[DbTags.id] != estilo][DbTags.number_of_albums].values
            nombres_artistas = data[data[DbTags.id] != estilo][DbTags.id].values

            StyleVisualization.piechart(n_albums_artistas, nombres_artistas)

        elif checkpoint.lower() == "proyecto":
            loggeo_principio_proceso(accion, "None", STYLES)
            feature_tag = str(input("Introduzca el nombre de la variable a comparar: "))
            StyleVisualization.swarmplot(feature_tag)

    elif accion.lower() == "generar":
        Generator.generar_cancion(estilo, cantante)

    else:
        logging.error("Acción no comtemplada")
