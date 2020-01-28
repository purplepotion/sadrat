# gets recent tweets using live_tweets.csv
import random
import pandas as pd

def get_tweet():
    """":param
    list of floats: (longitude, latitude) in degrees SW corner and NE corner
    """
    df = pd.read_csv("/Users/jarvis/Desktop/CODE/sadrat/web_app/appdata/adrmine_tweets_with_locations.csv")
    num = random.randrange(1,100,1)
    return ["Tweet:  " + df.iloc[num]["tweet"], df.iloc[num]["label_proba"]]