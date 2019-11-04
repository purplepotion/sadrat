import praw
import pandas as pd
import datetime as dt
from time import sleep  # Used for limiting API calls
from os.path import isfile

reddit = praw.Reddit(
    client_id="6bN05f96P-YKeQ",
    client_secret="CW4Tg6zoLVr206XCUsQMfz4C5pk",
    username="perplexed_v",
    password="reddit_scrapper",
    user_agent="reddit_scrapper",
)


class RedditScraper:
    """
        A class used to represent Reddit Scraper

        ...

        Attributes
        ----------
        sub: str
            the name of subreddit
        sort : str
            sort type for the subreddit
        limit : int
            the number of posts
        mode : str
            opening mode for csv file

        Methods
        -------
       set_sort()
            returns sort type of the subreddit
       get_posts()
            gets unique posts from subreddit and adds them to pandas dataframe(exported to CSV)
       get_date()
            converts scraped date and time of posts to UTC format
    """

    def __init__(self, sub, sort="new", limit=1000, mode="w"):
        """
              Parameters
              ----------
              sub : str
                  the name of subreddit
              sort : str
                  sort type for the subreddit
              limit : int
                  the number of posts
              mode : str
                  opening mode for csv file
        """
        self.sub = sub
        self.sort = sort
        self.limit = limit
        self.mode = mode

    def set_sort(self):
        """
           Returns sort type for the subreddit with default as sort = "new"
        """
        if self.sort == "new":
            return self.sort, reddit.subreddit(self.sub).new(limit=self.limit)
        elif self.sort == "top":
            return self.sort, reddit.subreddit(self.sub).top(limit=self.limit)
        elif self.sort == "hot":
            return self.sort, reddit.subreddit(self.sub).hot(limit=self.limit)
        else:
            self.sort = "new"
            print("Default sort is new")
            return self.sort, reddit.subreddit(self.sub).hot(limitit=self.limit)

    def get_posts(self):
        """
           Get unique posts from subreddit and add to pandas dataframe(exported to CSV)

        """

        sub_dict = {"title": [], "id": [], "text": [], "created": []}
        csv = f"posts.csv"

        # Sorting method.
        sort, subreddit = self.set_sort()

        # To check if CSV exists and has some data already
        df, csv_has = (pd.read_csv(csv), 1) if isfile(csv) else ("", 0)

        print(f"csv = {csv}")
        print(f"Sort = {sort} and sub = {self.sub}")
        print(f"csv_has = {csv_has}")

        print(f"Collecting information from r/{self.sub}.")
        for post in subreddit:

            # Check if post.id is in df and set to True if df is empty.
            # This way new posts are still added to dictionary when df = ''
            unique_id = post.id not in tuple(df.id) if csv_has else True

            # if id of post is unique i.e not added previously
            if unique_id:
                sub_dict["text"].append(post.selftext)
                sub_dict["title"].append(post.title)
                sub_dict["id"].append(post.id)
                sub_dict["created"].append(post.created)
            sleep(0.1)

        sub_data = pd.DataFrame(sub_dict)

        def get_date(created):
            """
               Converts scraped date and time to UTC format
            """

            return dt.datetime.fromtimestamp(created)

        _timestamp = sub_data["created"].apply(get_date)
        sub_data = sub_data.assign(timestamp=_timestamp)
        del sub_data["created"]
        sub_data.columns = ["title", "id", "text", "created"]

        # Add sub_data to df if df exists and export to csv file
        if "DataFrame" in str(type(df)) and self.mode == "w":
            pd.concat([df, sub_data], axis=0, sort=0).to_csv(csv, index=False)
            print(f"{len(sub_data)} new posts collected and added to {csv}")
        elif self.mode == "w":
            sub_data.to_csv(csv, index=False)
            print(f"{len(sub_data)} posts collected and saved to {csv}")
        else:
            print(
                f"{len(sub_data)} posts were collected but they were not "
                f'added to {csv} because mode was set to "{self.mode}"'
            )


if __name__ == "__main__":
    subreddits = [
        "healthcare",
        "HealthCareIT",
        "public_health",
        "globalhealth",
        "emergencymedicine",
    ]
    for name in subreddits:
        RedditScraper(name, limit=1000, mode="w", sort="new").get_posts()

