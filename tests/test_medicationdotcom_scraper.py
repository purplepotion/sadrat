import sys
sys.path.append('/Users/abhij/Desktop/Github/sadrat/')

import unittest
from scrapers.helpers import Webrequests
from bs4 import BeautifulSoup
from scrapers.medicationsdotcom_scraper import get_text_from_url
from scrapers.medicationsdotcom_scraper import get_all_urls
from scrapers.medicationsdotcom_scraper import get_comments
w = Webrequests()
drug = "levaquin"
url = "http://medications.com/" + drug
raw_html = w.simple_get(url)
html = BeautifulSoup(raw_html, 'html.parser')

class TestMedicationdotcom_scraper(unittest.TestCase):
    global w
    global drug
    global url
    global raw_html
    global html
    def test_get_comments(self):
        result = get_comments("levaquin")
        self.assertIsNotNone(result)
    def test_get_all_urls(self):
        result = get_all_urls(html)
        self.assertIsNotNone(result)
    def test_get_text_from_url(self):
        result = get_text_from_url("/levaquin/Levaquin-Cipro-Trovan-now-Im-mess")
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
