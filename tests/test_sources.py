import unittest
from app.models import Sources

class TestSources(unittest.TestCase):
    '''
    Test Class behaviour of Sources class 
    '''
    def setUp(self):
        self.new_sources = Sources('your-news', 'Your News', 'Your trusted news provider in Uganda', 'https://your-news.com','business','ug')
        
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))