from nltk import FreqDist


def show_freqdist(data):
    freqdist = FreqDist(data)
    freqdist.plot(25, cumulative=False)