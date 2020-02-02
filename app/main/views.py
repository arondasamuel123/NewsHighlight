from flask import render_template
from . import main
from ..requests import get_sources,get_articles


@main.route('/')
def index():
    '''
    Root page function 
    '''
    general_news = get_sources('general')
    business_news = get_sources('business')
    sports_news = get_sources('sports')
    # print(general_news)
    return render_template('index.html', general=general_news, business = business_news, sports = sports_news)

@main.route('/articles/<news_id>')
def fetch_articles(news_id):
    '''
    Fetch articles based on the source id
    '''
    articles = get_articles(news_id)
    #print(articles)
    return render_template('articles.html', articles = articles)