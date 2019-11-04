# SADRAT - Smart Adverse Drug Reaction Assessment Tools

## Overview
There is enough research evidence that social media can be an important source of indicating Adverse Drug Reactions and analyzing disease trends in a population. Although this signal is weak, many algorithms have been developed to extract the important signals that depict a valid ADR. However, the prediction of future disease trends from social media data in a population under study is a challenging task and breakthroughs have not been made in this direction. Also, another epidemiologic challenge that demands to be solved is predicting possible reason(s) behind the appearance of such trends for further verification and validation of the Early Warning System.
Hence, **SADRAT** would tackle the above-mentioned issues providing the pharmaceutical companies with the necessary parameters and predictive outcomes (i.e. Disease trends, probable reasons for disease etc. using predictive analytics) in a dashboard that would leverage their decision-making (related to marketing strategies, venturing into new market and the introduction of new and upgraded drugs) while targeting a particular population based on pivots such as season, age, gender, race, etc. 

## Technology Components and Technical Stack:
#### Components:
* Data Miner/Crawler
* Database
* Preprocessor
* Custom Algorithms
* API - to connect to frontend
* Dashboard
#### Technical Stack:
* Python - General Programming Language
* MongoDB - non-relational database
* Flask - backend
* Dash/Plotly - for dashboard frontend
* PyMedTermino

## Approach:
#### Text Mining:
A **TEXT MINER** component would be responsible for extracting the unstructured text through the different APIs of the social media platforms. We will mine through a large number of sites where medical conversations take place. Some of the sites will be some selected Reddit channels, Twitter, DailyStrength, etc. We will not only mine the text but also other personal(public) and location-specific information that can be mined along with it. This data will then be preprocessed and saved in an external database for further analysis.
#### Preprocessing:
**Preprocessing** includes the cleaning and labeling of the possible ADR. Cleaning includes the removal of stopwords and lemmatization. We will use PyMedTermino to extract any text that contains a medical term by querying the same in UMLS (we are not checking whether its an ADR or not in this step) and then save it in the database.
#### Analytics:
##### 1. Predictive Analysis of Disease Trends:
The future disease trend (location-wise) would be predicted from historical data using Deep learning algorithms. LSTMs have been used to predict time-series data such as this and have performed well in predicting stock market trends. Hence we believe that it can be a good baseline for starting future disease trend prediction from historical data sampled from social media.
##### 2. Demographic Analysis of Disease Trends:
This is the most unique and exciting part of the project where we will try to present the different demographic features that might have any co-relation with the disease trend of the location and lead to a health outcome. For example, the common cold might be a very common condition of a location during a particular season or due to a particular population habit like food habits or air pollution index. Such data might be extracted from social media as well. Hence our text miner will also look for these things from the texts mined from that location and present it in the dashboard in the form of a FEED which will allow pharma companies to make a decision based on population habits.
#### ADR likelihood metrics calculation:
The extracted ADRs will be scored based on a custom algorithm built upon the Naranjo algorithm. The ADRs will then be verified with the pre-existing known ADRs from the SIDER (database of drugs and side effects) project. The cumulative likelihood score would then be calculated and displayed on the dashboard for all the known ADRs for the given location.
#### Dashboard:
We will use **dash** and **plotly** libraries, which use flask backend in order to display the results from our analysis.
