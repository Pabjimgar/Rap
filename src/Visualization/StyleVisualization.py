from wordcloud import WordCloud, STOPWORDS
from Preprocessing.Tags import DbTags
from Preprocessing import Database_ops
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

stopwords = set(STOPWORDS)
fig = plt.figure(1, figsize=(12, 12))
ESTILOS = ["Flamenco", "Indie", "Latino", "Pop", "Rock", "Rap"]
columns = ['_id', 'max_words_per_song', 'min_words_per_song', 'number_of_albums', 'number_of_songs',
           'number_of_stopwords', 'percentage_of_relevant_words', 'text_no_sw', 'text_raw', 'unique_words',
           'word_average_per_song', "style"]

tags = DbTags


def show_wordcloud(data, title=None):
    """"""

    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=50,
        max_font_size=40,
        scale=3,
        collocations=False
    ).generate(str(data))

    plt.axis('off')
    if title:
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.show()


def compare_artists(lyrics_data, estilo):
    """Función diseñada para comparar los artistas dentro cada estilo entre sí y con el estilo en si mismo"""

    artist_data = lyrics_data[lyrics_data["_id"] != estilo]
    style_data = lyrics_data[lyrics_data["_id"] == estilo]

    artist_data.plot(kind="bar", x="_id", y=["max_words_per_song", "word_average_per_song",  "min_words_per_song"])

    plt.axhline(y=style_data.iloc[0]["max_words_per_song"], color='b', linestyle='-')
    plt.axhline(y=style_data.iloc[0]["word_average_per_song"], color='r', linestyle='-')
    plt.axhline(y=style_data.iloc[0]["min_words_per_song"], color='g', linestyle='-')

    plt.show()


def swarmplot(feature_tag=tags.percentage_of_relevant_words):
    """Función para generar un swarmplot que muestre diferentes variables"""

    length_tags = ["text_raw", "text_no_sw", "unique_words"]

    sns.set_style("whitegrid")
    df = pd.DataFrame(columns=columns)

    for estilo in ESTILOS:

        stats = Database_ops.set_style_collection(estilo).find()
        data = pd.DataFrame(list(stats))
        data["style"] = estilo
        df = df.append(data, ignore_index=True)

    df = df[df[tags.id] != df["style"]]

    if feature_tag in length_tags:
        df[feature_tag] = df[feature_tag].str.len()

    df = df[[tags.id, "style", feature_tag]]

    melted_df = pd.melt(df, id_vars=[tags.id, "style"], var_name="tag").dropna(axis=0)

    with sns.color_palette(
            ["#8ED752", "#F95643", "#53AFFE", "#C3D221", "#BBBDAF", "#AD5CA2", "#F8E64E"], n_colors=56, desat=.9):
        plt.figure(figsize=(12, 10))
        sns.swarmplot(x="style", y="value", data=melted_df, hue="_id", split=True, size=7)
        plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0)
        plt.show()


def piechart(data, labels):
    """Función para generar un gráfico de tarta con los datos de los albumes"""

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')

    plt.show()
