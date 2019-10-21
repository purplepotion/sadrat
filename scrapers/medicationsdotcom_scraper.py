# Written By - Shaswat Lenka
# DATE: 22nd October 2019
# Code Review Requested.

from scrapers.helpers import Webrequests
from bs4 import BeautifulSoup


# Get the drug name from a drug database
# Get all the discussions regarding the drug from medications.com
# Preprocess and save the same to disc

# testing for a single drug
# TODO: write a function to get the drug name dynamically from a source

def get_comments(drugname):

    w = Webrequests()
    drug = drugname
    url = "http://medications.com/" + drug
    raw_html = w.simple_get(url)
    text_corpus = list()
    if raw_html is not None:
        html = BeautifulSoup(raw_html, 'html.parser')
        list_comments = html.select("span", class_="post-enter")
        if len(list_comments) > 0:
            for comment in list_comments:
                text_corpus.append(comment.text)

        else:
            # raise Exception if no comments found for the given drug
            raise Exception("No comments found for {} at medications.com".format(drug))
    else:
        # raise an exception if we failed to get any data from url
        raise Exception("Error retrieving contents from {}".format(url))

    return text_corpus


levaquin = get_comments("levaquin")
print(levaquin)





