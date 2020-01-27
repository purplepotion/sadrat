#!/usr/bin/env python

import json
import spacy
import scispacy
import pandas as pd
from scispacy.umls_linking import UmlsEntityLinker

nlp = spacy.load("en_ner_bc5cdr_md")

drugs_df = pd.read_csv(r"D:\Events\GE Hackathon\sadrat\additional resources\drug.csv")
drugs_df.drop(['drug_id', 'drugbank_id', 'pubchem_cid'], axis=1, inplace=True)
drugs_df.dropna(axis=0, inplace=True)
drugs_df.head()

with open(r"D:\Events\GE Hackathon\sadrat\additional resources\drug_disease.json", "r") as file:
    drug_disease = json.load(file)


def get_chemical(common_name):
    """
    This function takes in the common name of any drug as an argument
    and returns its chemical name.

    Parameters:
    common_name (str): Common Name of any drug as a string.

    Returns:
    chemical_name (str): Chemical Name of the given drug.

    """
    chemical_name = None
    for i in range(len(drugs_df.name)):
        if common_name in drugs_df.iloc[i]['alias']:
            chemical_name = drugs_df.iloc[i]['name']
    if chemical_name is None:
        common_name = ' '.join([word.capitalize() for word in common_name.split()])
        for i in range(len(drugs_df.name)):
            if common_name in drugs_df.iloc[i]['alias']:
                chemical_name = drugs_df.iloc[i]['name']
    return chemical_name


def get_disease(drug):
    """
    This function takes in the chemical name of any drug as an argument
    and returns all the possible diseases, the drug can be prescribed for.

    Parameters:
    drug (str): Chemical Name of any drug as a string.

    Returns:
    disease (list): List of all possible diseases.
    """
    disease = None
    if drug in drug_disease.keys():
        disease = sorted(drug_disease[drug])
    drug = ' '.join([word.capitalize() for word in drug.split()])
    if drug in drug_disease.keys():
        disease = sorted(drug_disease[drug])
    drug = get_chemical(drug)
    if drug in drug_disease.keys():
        disease = sorted(drug_disease[drug])
    return disease


def disease_from_tweet(tweet):
    """
    This function takes in a tweet or any other string as an argument
    and returns its possible disease related to the tweet.

    Parameters:
    tweet (str): A tweet or a string.

    Returns:
    diseases (list): List of all probable diseases.
    """
    doc = nlp(tweet)
    drugs = []
    diseases = []
    for entity in doc.ents:
        drug = entity.text
        label = entity.label_
        if label == "CHEMICAL" and drug not in drugs:
            diseases.extend(get_disease(drug))
        elif label == "DISEASE" and drug not in drugs:
            diseases.append(drug)
        drugs.append(drug)
    return diseases


# text = 'My doctor prescribed me lisinopril because my BP was a little high.  I took the pill for 2 days and noticed ' \
#         'a small mosquito looking bump in the center of my top lip.  About 3 hours later my lip was so big & numb I ' \
#         'immediately went to the ER to find out lisinopril was the cause of it.  This is ridiculous Im embarrassed to ' \
#         'go any place because of my lip. If any one is thinking about starting a law suite you can count me in. ... ' \
#         'more »My doctor prescribed me lisinopril because my BP was a little high.  I took the pill for 2 days and ' \
#         'noticed a small mosquito looking bump in the center of my top lip.  About 3 hours later my lip was so big & ' \
#         'numb I immediately went to the ER to find out lisinopril was the cause of it.  This is ridiculous Im ' \
#         'embarrassed to go any place because of my lip. If any one is thinking about starting a law suite you can ' \
#         'count me in. '
#
# disease_from_tweet(text)
