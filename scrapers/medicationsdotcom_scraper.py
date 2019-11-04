# Written By - Shaswat Lenka
# DATE: 22nd October 2019
# Code Review Requested.

from scrapers.helpers import Webrequests
from bs4 import BeautifulSoup
import csv


# Get the drug name from a drug database
# Get all the discussions regarding the drug from medications.com
# Preprocess and save the same to disc

# testing for a single drug
# TODO: write a function to get the drug name dynamically from a source

def get_all_urls(html):
    """
    gets the url of all the comments in a drug page
    @params:
    html: BeautifulSoup object
    drugname: String

    @returns: list()
    """
    urls = list()
    for title in html.find_all("span", class_="post-title"):
        urls.append(title.a['href'])

    return urls


def get_text_from_url(url):
    """get the text from a given comment url
    @params: url - String (here I assume that it is in the same format as the 'urls' of the return value of get_all_urls
    @returns: String - text corpus
    """
    full_url = "http://medications.com" + url
    w = Webrequests()
    raw_html = w.simple_get(full_url)
    html = BeautifulSoup(raw_html, 'html.parser')

    first_content = html.find("span", class_="first_content")
    if first_content is not None:
        first_content_text = first_content.p.text
    else:
        return None

    more_content = html.find("span", class_="more_content")
    if more_content is not None:
        more_content_text = more_content.p.text
    else:
        return None

    return first_content_text + more_content_text


def get_comments(drugname):
    """Get the discussions and comments on medications.com about the given drug
    @params:
        drugname - String representing the drug name
    @returns:
        list() of all text based comments on the given drug
    """

    w = Webrequests()
    drug = drugname
    url = "http://medications.com/" + drug
    raw_html = w.simple_get(url)
    text_corpus = list()
    if raw_html is not None:
        html = BeautifulSoup(raw_html, 'html.parser')

        # list of all urls that posts titles of the given drug
        urls = get_all_urls(html)

        for url in urls:
            text = get_text_from_url(url)
            if text is not None:
                text_corpus.append(text)
            else:
                continue
    else:
        # raise an exception if we failed to get any data from url
        raise Exception("Error retrieving contents from {}".format(url))

    return text_corpus


def save_to_disk(text_corpus, drugname):
    """save the scrapped text to csv
    @params:
    """
    with open("/Users/jarvis/Desktop/CODE/sadrat/datasets/medications_dot_com_data.csv", 'a') as file:
        for i in range(len(text_corpus)):
            row = [i, drugname, text_corpus[i]]
            writer = csv.writer(file)
            writer.writerow(row)
    file.close()


# Driver Code
druglist = ["lisinopril", "avelox", "prednisone", "cipro", "floxin", "elavil", "norvasc", "cozaar", "hyzaar", "femara",
            "methylpred-dp","aricept", "versed", "questran", "welchol", "venofer", "avalide", "topamax", "yaz", "geodon"
            , "warfarin-sodium"]
for drug in druglist:
    comments = get_comments(drug)
    save_to_disk(comments, drug)