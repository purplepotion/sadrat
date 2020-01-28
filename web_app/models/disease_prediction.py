#!/usr/bin/env python

import json
import spacy
import scispacy
import pandas as pd
from scispacy.umls_linking import UmlsEntityLinker

nlp = spacy.load("en_ner_bc5cdr_md")

drugs_df = pd.read_csv("/Users/jarvis/Desktop/CODE/sadrat/additional resources/drug.csv")
drugs_df.drop(['drug_id', 'drugbank_id', 'pubchem_cid'], axis=1, inplace=True)
drugs_df.dropna(axis=0, inplace=True)
drugs_df.head()

with open("/Users/jarvis/Desktop/CODE/sadrat/additional resources/drug_disease.json", "r") as file:
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


def disease_matching(diseases_lists):
    """
    Parameters:
        *argv: All lists about probable diseases from multiple sources.

    Returns:
        diseases: List of diseases which are most common or most probable.
    """
    diseases = set(diseases_lists[0])
    for dis in diseases_lists:
        dis = set(dis)
        diseases = diseases.intersection(dis)
    return diseases


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
    ds = []
    diseases = []
    for entity in doc.ents:
        drug = entity.text
        label = entity.label_
        if label == "CHEMICAL" and drug not in drugs:
            if get_disease(drug) is not None:
                diseases.append(get_disease(drug))
        elif label == "DISEASE" and drug not in drugs:
            ds.append(drug)
        drugs.append(drug)
    if len(ds):
        ds = [d.capitalize() for d in ds]
        diseases.append(ds)
    if len(diseases) == 1:
        return ds
    if diseases == []:
        return []
    else:
        return list(disease_matching(diseases))
if __name__ == '__main__':
    disease_from_tweet("That said it's become too much recently and I've caved and agreed to go see a dietician :(")