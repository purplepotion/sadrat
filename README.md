# SADRAT - Smart Adverse Drug Reaction Assessment Tools

## Research Overview
There is enough research evidence that social media can be an important source of indicating Adverse Drug Reactions and analyzing disease trends in a population. Although this signal is weak, many algorithms have been developed to extract the important signals that depict a valid ADR. However, the prediction of future disease trends from social media data in a population under study is a challenging task and breakthroughs have not been made in this direction. Also, another epidemiologic challenge that demands to be solved is predicting possible reason(s) behind the appearance of such trends for further verification and validation of the Early Warning System.

Hence, **SADRAT** would tackle the above-mentioned issues providing the pharmaceutical companies with the necessary parameters and predictive outcomes (i.e. Disease trends, probable reasons for disease etc. using predictive analytics) in a dashboard that would leverage their decision-making (related to marketing strategies, venturing into new market and the introduction of new and upgraded drugs) while targeting a particular population based on pivots such as season, age, gender, race, etc. 

#### Installing Spacy
To correctly instal spacy, run these command in sequence in your Virtual environment
to avoid getting runtime exceptions.
<br>`pip install spacy` <br>
`python -m spacy download en`<br>

### Installing TextBlob
`pip install textblob`<br>
`python -m textblob.download_corpora`

### Setting up the Jupyter Notebook Development Environment for Research:
`pip install jupyter`  - In your virtual environment
`ipython kernel install --user --name=yourvirtualenvname` - To add a jupyter kernel
 