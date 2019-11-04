from Visualization import MongoReader
from Preprocessing import Spanish_corpus
from Preprocessing import Counting_class

if __name__ == '__main__':

    lista_de_palabras = MongoReader.read_from_mongo("Nach")
    lista_de_palabras_limpia = Spanish_corpus.remove_stopwords(lista_de_palabras)

    a = Counting_class.calculate_number_of_stopwords(lista_de_palabras, lista_de_palabras_limpia)

    print(a)
