import datetime as dt
import pandas as pd
import praw
import csv
import json


init_reddit = praw.Reddit(client_id='6bN05f96P-YKeQ',
                          client_secret='CW4Tg6zoLVr206XCUsQMfz4C5pk',
                          username='perplexed_v',
                          password='reddit_scrapper',
                          user_agent='reddit_scrapper')

name_subreddit1 = init_reddit.subreddit('public_health')
name_subreddit2 = init_reddit.subreddit('emergencymedicine')
name_subreddit3 = init_reddit.subreddit('globalhealth')
name_subreddit4 = init_reddit.subreddit('HealthCareIT')
name_subreddit5 = init_reddit.subreddit('healthcare')

hot_subreddit1 = name_subreddit1.search('drug')
hot_subreddit2 = name_subreddit2.search('drug')
hot_subreddit3 = name_subreddit3.search('drug')
hot_subreddit4 = name_subreddit4.search('drug')
hot_subreddit5 = name_subreddit5.search('drug')

data_dict = {"title": [], "comments_num": [], "body": []}

for submission in hot_subreddit1:
    data_dict["title"].append(submission.title)
    data_dict["comments_num"].append(submission.num_comments)
    data_dict["body"].append(submission.selftext)

for submission in hot_subreddit2:
    data_dict["title"].append(submission.title)
    data_dict["comments_num"].append(submission.num_comments)
    data_dict["body"].append(submission.selftext)

for submission in hot_subreddit3:
    data_dict["title"].append(submission.title)
    data_dict["comments_num"].append(submission.num_comments)
    data_dict["body"].append(submission.selftext)

for submission in hot_subreddit4:
    data_dict["title"].append(submission.title)
    data_dict["comments_num"].append(submission.num_comments)
    data_dict["body"].append(submission.selftext)

for submission in hot_subreddit5:
    data_dict["title"].append(submission.title)
    data_dict["comments_num"].append(submission.num_comments)
    data_dict["body"].append(submission.selftext)

with open('sampledata.csv', 'w', encoding='utf-8') as file:
    w = csv.DictWriter(file, data_dict.keys())
    w.writeheader()
    w.writerow(data_dict)

with open('sampledata.json', 'w', encoding='utf-8') as file1:
    json.dump(data_dict, file1)





