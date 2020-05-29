from nltk import FreqDist
from math import pi
import matplotlib.pyplot as plt


def show_freqdist(data):
    freqdist = FreqDist(data)
    freqdist.plot(25, cumulative=False)


def show_spider_graph(data):

    attributes = list(data)[1:]
    attno = len(attributes)

    values = data.iloc[0].tolist()
    name_of_band = values.pop(0)

    values += values[:1]

    angles = [n / float(attno) * 2 * pi for n in range(attno)]
    angles += angles[:1]

    ax = plt.subplot(111, polar=True)

    # Add the attribute labels to our axes
    plt.xticks(angles[:-1], attributes)

    # Plot the line around the outside of the filled area, using the angles and values calculated before
    ax.plot(angles, values)

    # Fill in the area plotted in the last line
    ax.fill(angles, values, 'teal', alpha=0.1)

    # Give the plot a title and show it
    ax.set_title(name_of_band)
    ax.set_ylim(0, 38000)
    plt.show()
