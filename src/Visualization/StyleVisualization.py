from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

stopwords = set(STOPWORDS)
fig = plt.figure(1, figsize=(12, 12))


def show_wordcloud(data, title = None):
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

    """Función diseñada para comparar los artistas de cada estilo entre sí y con el estilo en si mismo"""

    artist_data = lyrics_data[lyrics_data["_id"] != estilo]
    style_data = lyrics_data[lyrics_data["_id"] == estilo]

    artist_data.plot(kind="bar", x="_id", y=["max_words_per_song", "word_average_per_song",  "min_words_per_song"])

    plt.axhline(y=style_data.iloc[0]["max_words_per_song"], color='b', linestyle='-')
    plt.axhline(y=style_data.iloc[0]["word_average_per_song"], color='r', linestyle='-')
    plt.axhline(y=style_data.iloc[0]["min_words_per_song"], color='g', linestyle='-')

    plt.show()
