import unittest
import urllib.request
from app.models import Articles


class TestArticle(unittest.TestCase):
    
    def setUp(self):
        '''
        Test Class to test the behaviour of the Article class
        '''
        self.new_articles = Articles("Samuel Aronda", "Flask", "Great to begin Flask","https://www.url.com", "https://url/sa.jpg",  "2020-01-27")
        
    def test_instance(self):
        '''
        Test to check if self.new_articles is an instance of the Articles class
        '''
        self.assertTrue(isinstance(self.new_articles,Articles))
        
    def test_response(self):
        response = urllib.request.urlopen('https://newsapi.org/v2/everything?sources=abc-news&apiKey=a4755d1d552c4b40a8982161114c43b9')