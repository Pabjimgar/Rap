import os
import markovify


def print_song(path):

    with open(path) as f:
        text = f.read()
    # Build the model.
    text_model = markovify.Text(text)

    # Print five randomly-generated sentences
    for i in range(5):
        print(text_model.make_sentence())


def generar_cancion(estilo, cantante=""):

    base_path = "/home/pablojimenez/PycharmProjects/Rap/src/Scrapping/letra_canciones/" + estilo + "/"
    singer_path = base_path + cantante + ".txt"

    if cantante == "":

        with open(base_path + estilo + 'temp.txt', 'a') as fileEnd:
            for file in os.listdir(base_path):
                with open(base_path + file, 'r') as fileRead:
                    illo = fileRead.read()
                    fileEnd.write(illo)

        print_song(base_path + estilo + 'temp.txt')

    else:

        print_song(singer_path)

