# gets recent tweets using live_tweets.csv

import pandas as pd

def get_tweet():
    """":param
    list of floats: (longitude, latitude) in degrees SW corner and NE corner
    """
    df = pd.read_csv("/Users/jarvis/Desktop/CODE/sadrat/web_app/appdata/adrmine_tweets_with_locations.csv")
    return "Tweet:  " + df.iloc[-1]["tweet"]
