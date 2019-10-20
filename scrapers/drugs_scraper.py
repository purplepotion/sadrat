import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
import time
import pickle

all_drugs = []
alphabets = 'abcdefghijklmnopqrstuvwxyz'
drugs_url_dict = {}

for alphabet in alphabets:
    # time.sleep(3)
    url = "https://www.drugs.com/alpha/" + alphabet + ".html"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    drugs_list = soup.find(class_="ddc-list-column-2").find_all("li")

    for drug in drugs_list:
        drug_name = drug.get_text()
        drug_url = drug.find('a')['href']
        drugs_url_dict[drug_name] = drug_url
        print(drug_name + ": " + drug_url)

drug_adr_dict = {}

for drug, drug_url in drugs_url_dict.items():

    drug_name = drug
    url = "https://www.drugs.com" + drug_url

    # time.sleep(3)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    side_effects = soup.find(id="SideEffects")
    if side_effects is None:
        side_effects = soup.find(id="sideEffects")

    try:
        most_common_adr = side_effects.find_next_sibling("ul").find_all("li")
    except AttributeError:
        continue

    drug_adrs = []
    for adr in most_common_adr:
        adverse_events = adr.get_text().replace(";", "").replace(".", "")
        drug_adrs.append(adverse_events.strip())

    drug_adr_dict[drug_name] = drug_adrs

# pp(drug_adr_dict)

file = open("drug_adr", "wb")
pickle.dump(drug_adr_dict, file)
file.close()
