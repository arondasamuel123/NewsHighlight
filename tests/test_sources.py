import unittest
import urllib.request
from app.models import Sources

class TestSources(unittest.TestCase):
    '''
    Test Class behaviour of Sources class 
    '''
    def setUp(self):
        self.new_sources = Sources('your-news', 'Your News', 'Your trusted news provider in Uganda', 'https://your-news.com','business','ug')
        
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))
        
    def test_response(self):
        '''
        Test to see if response is okay from api
        '''
        response = urllib.request.urlopen('https://newsapi.org/v2/sources?apiKey=a4755d1d552c4b40a8982161114c43b9')
        self.assertTrue(response)