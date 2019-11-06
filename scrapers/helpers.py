from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


class Webrequests:
    """
    Tools to download web pages
    Code Credits - realpython.com

    """

    def __init__(self):
        pass

    def simple_get(self, url):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with closing(get(url, stream=True)) as resp:
                if self.is_good_response(resp):
                    return resp.content
                else:
                    return None

        except RequestException as e:
            self.log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None

    def is_good_response(self, resp):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)

    def log_error(self, e):
        """
        It is always a good idea to log errors.
        This function just prints them, but you can
        make it do anything.
        """
        print(e)


class Preprocessing:
    """contains preprocessing methods for NLP"""

    def __init__(self):
        pass

    def custom_preprocessor(self, text):
        """
        @TODO - Write tests for this function
        convert all letters to lower case
        remove all numbers and special characters
        remove punctuations, accent marks etc
        remove stop words
        lemmatize all words

        @params: text - str
        @returns: list of preprocessed words

        """
        if type(text) != str:
            raise Exception("a string is expected to be passed but instead, {} was passed".format(type(text)))

        if text == "":
            raise Exception("An empty string was passed which was not expected")

        stop_list = set(stopwords.words('english'))
        text = text.lower()  # convert to lowercase
        text = re.sub(r'\d+', '', text)  # remove numbers
        text = re.sub('[!#$?,.:";]', '', text)  # remove punctuation
        text = text.strip()  # remove additional whitespace
        word_tokens = word_tokenize(text)
        filtered_sentence = [x for x in word_tokens if not x in stop_list]
        stemmer = PorterStemmer()
        corpus = []
        for word in filtered_sentence:
            corpus.append(stemmer.stem(word))

        return corpus

    def simple_preprocessor_string(self, text):
        """
        same as custom preprocessor but without lemmatization and
        returns a preprocessed string instead of a list of words
        :param text: type(text): str
        :return: str
        """
        if type(text) != str:
            raise Exception("a string is expected to be passed but instead, {} was passed".format(type(text)))

        if text == "":
            raise Exception("An empty string was passed which was not expected")

        stop_list = set(stopwords.words('english'))
        text = text.lower()  # convert to lowercase
        text = re.sub(r'\d+', '', text)  # remove numbers
        text = re.sub('[!#$?,.:";]', '', text)  # remove punctuation
        text = text.strip()  # remove additional whitespace
        word_tokens = word_tokenize(text)
        filtered_wordlist = [x for x in word_tokens if not x in stop_list]
        filtered_sentence = ""
        for word in filtered_wordlist:
            filtered_sentence = filtered_sentence + word + " "

        return filtered_sentence






