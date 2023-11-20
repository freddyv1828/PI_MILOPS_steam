import pandas as pd
import datetime as dt
import re
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Funcion analisis de sentimiento
def analisis_sentimiento(review):

    if review is None:
        return 1

    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(review)
    compound = score["compound"]

    # Utilizar un umbral más preciso
    if compound < -0.4:
        return 0
    elif compound > 0.4:
        return 2
    else:
        return 1