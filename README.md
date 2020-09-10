# SADRAT - Smart Adverse Drug Reaction Assessment Tools

## 📕Contribution Guidelines for [FOSSHACK 2020](https://fossunited.org/project?project=SADRAT) 
#### 1. History and Motivation
This project was started in Autumn Session 2019 by a research group at [National Institute of Technology Rourkela](https://www.nitrkl.ac.in/)
under the guidance of Prof. B.P. Nayak(the same group that runs purplepotion) of Regenerative and Rehabilitative Medicine Laboratory, Department of 
Biomedical Engineering. The motivation behind this research is to improve the performance of 
the state-of-the art ML and DL models to detect Adverse Drug Reaction Signals(ADRS) from
social media platforms like Twitter using the concept of [**Data Programming**](https://arxiv.org/abs/1605.07723#:~:text=We%20therefore%20propose%20a%20paradigm,are%20noisy%20and%20may%20conflict.) .<br>
**How it might look like:** <br>
**Sample Tweet:** <br>
`Tweet: "Having Headaches since morning! I need to get off of crocin!"` <br>
**Sample Result:**<br>
`ADR Probability: 88%`<br>
`Detected Drug: Crocin`<br>
`Detected ADR: Headache`<br>
This was quite an easy one to guess. But in real scenarios, sentence structures can be very complicated.
One of the major improvements and novelty we want to bring in the pipeline of performing such tasks
is to remove the human involvement in preparing a labelled dataset in order to perform supervised learning,
instead, we want to make the process programming weakly supervised strategies and at the same time reducing the noise generated
during the process to a minimum. The above classification might seem a simple enough task for a 
modern classifier. But, the bigger challenge that we are attempting to solve here are the following:<br>
1. Creating a minimum noise, labelled training set for supervised classification.
2. Removing direct manual involvement in preparing the golden training and testing datasets.
3. Creating a highly scalable programmable alternative to maximize performance and minimize time required to 
generate labelled training sets.<br>
Finally, we would develop a web app around the models to interact with them from the client side.

#### 2. Prerequisite Knowledge
1. A basic knowledge of Machine Learning(ML) and mathematics involved in ML.
2. An intermediate knowledge in Python (3.x) Programming Language. i.e. you should comfortable with 
OOP, Web development with flask, working with APIs, libraries and frameworks. 
3. Project specific knowledge (discussed in 3.)

#### 3. Project Specific Prerequisites:
1. Learn about Data Programming from [here](https://arxiv.org/abs/1605.07723#:~:text=We%20therefore%20propose%20a%20paradigm,are%20noisy%20and%20may%20conflict.).
2. Learn about Snorkel from [here](https://www.snorkel.org/)
3. Learn about [flask](https://flask.palletsprojects.com/en/1.1.x/) and [dash](https://dash.plotly.com/) - for contributing to the web app

#### What if I don't have any prerequisite knowledge? How can I contribute?
Each an every person reading this is a potential contributor for us. We have contribution opportunities for everyone irrespective of knowledge and experience. You can contribute.<br>
1. For complete beginners having **no previous programming knowledge**: If you have spent some time reading about the project and what we are willing to achieve, you can contribute to the docs. You 
can help us spread the word about this project and help us get more people involved :)
2. People with Knowledge of Python but no ML knowledge: You can contribute to the web app. See (2.) above.
3. People with Knowledge of Python and ML: you should be able to contribute to each and everything we are working on here!<br>

>What else will I get?<br>
Friends! We are people from diverse backgrounds and interests. Some are even working/incoming FTEs in well known software firms. This would be a great way to know each other and contribute to a single cause!

**NOTE**: Every contributor is valuable to us. Hence each and every contributor irrespective of the contribution, would be mentioned in the "contributors" section of the page.

##### COMMUNICATION
All communications regarding FOSSHACK 2020 would take place in the #fosshack2020 Slack Channel : [LINK](https://join.slack.com/t/purplepotion/shared_invite/zt-harse3jn-LZGNpcSUJE5XFyvJfa~57Q) (expires in 30 days, i.e on 10th October 2020)

#####👨‍💻 Contributors 👩‍💻:
** _Author_ **: [Shaswat Lenka](https://github.com/ShaswatLenka)<br>
Top Contributors: [Debabrata Panigrahi](https://github.com/Debanitrkl),  [Ankit Samota](https://github.com/ankitkumarsamota121), [Vedant Raghuwanshi](https://github.com/007vedant), [Abhijeet Sahoo](https://github.com/abhijeet2298), [Roshan Kumar Shaw](https://github.com/roshankshaw)<br>
___
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
`pip install jupyter`  - In your virtual environment <br>
`ipython kernel install --user --name=yourvirtualenvname` - To add a jupyter kernel
 