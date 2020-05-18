from wordcloud import WordCloud, STOPWORDS
from Preprocessing.Tags import DbTags
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

stopwords = set(STOPWORDS)
fig = plt.figure(1, figsize=(12, 12))

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


def swarmplot(data):
    """"""

    sns.set_style("whitegrid")

    data_graph = pd.melt(data, id_vars=[
        tags.id,
        tags.text_raw,
        tags.text_no_sw,
        tags.unique_words,
        tags.number_of_songs,
        tags.word_average_per_song,
        tags.number_of_stopwords,
        tags.percentage_of_relevant_words,
        tags.max_words_per_song,
        tags.min_words_per_song,
        tags.number_of_albums,
    ], var_name="Stat")

    with sns.color_palette([
        "#8ED752", "#F95643", "#53AFFE", "#C3D221", "#BBBDAF",
        "#AD5CA2", "#F8E64E", "#F0CA42", "#F9AEFE", "#A35449"], n_colors=10, desat=.9):
        plt.figure(figsize=(12, 10))
        # for tag in Tags:
        #     if tag == "_id":
        #         pass
        #     else:
        sns.swarmplot(x="Stat", y="value", data=data_graph, hue="_id", split=True, size=7)
        plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0)
        plt.show()


def pieChart(data, labels):
    """Función para generar un gráfico de tarta con los datos de los albumes"""

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')

    plt.show()
