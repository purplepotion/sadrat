import tweepy
import json
import csv
import pandas as pd
from pandas.io.json import json_normalize
from datetime import datetime, timedelta


class StreamListener(tweepy.StreamListener):
    """tweepy.StreamListener is a class provided by tweepy used to access
    the Twitter Streaming API to collect tweets in real-time.
    """

    def on_connect(self):
        """Called when the connection is made"""

        print("You're connected to the streaming server.")

    def on_error(self, status_code):
        """This is called when an error occurs"""

        print('Error: ' + repr(status_code))
        return False

    def on_data(self, data):
        """This will be called each time we receive stream data"""


        # Decode JSON
        datajson = json.loads(data)
        dd = json_normalize(datajson)
        dd.drop(dd.iloc[:, 4:], inplace = True, axis = 1)
        dd.drop(dd.columns[[1]], axis = 1, inplace = True)




        # 'training_tweets_collection' does not exist it will be created.
        if "lang" in datajson and datajson["lang"] == "en" and datajson['geo'] != "":
            print(datajson["text"])
            dd.to_csv('file1.csv', mode='a', header=False)



def obj_func(coordinates):
    # These are provided to you through the Twitter API after you create a account
    consumer_key = "hdeLGF1xnuvmMS7zMG2rkRrH8"
    consumer_secret = "GP0Kjp6iiPdG7L0MmZ1kLrRQLBVAdiNlnauqCE1CaemHXk68sq"
    access_token = "2463420950-kQ3Uq3qfa0bK4AQaa2uunI6CLeeq50qkNkyufZp"
    access_token_secret = "2ifpszLvRzthiW0FhDPXMNgmYfsifVurNchUBWJBbDXfh"

    auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth1.set_access_token(access_token, access_token_secret)

    # LOCATIONS are the longitude, latitude coordinate corners for a box that restricts the
    # geographic area from which you will stream tweets. The first two define the southwest
    # corner of the box and the second two define the northeast corner of the box.
    stream_listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
    stream = tweepy.Stream(auth=auth1, listener=stream_listener)
    stream.filter(locations=coordinates)


if __name__ == "__main__":
    coordinates = list(map(float, input().split()))
    obj_func(coordinates)
