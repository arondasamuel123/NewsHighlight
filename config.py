import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    API_KEY = os.environ.get('API_KEY')
    

class ProdConfig(Config):
    '''
    Production config child class
    '''


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}