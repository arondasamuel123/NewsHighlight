from flask import render_template
from . import main
from ..requests import get_sources


@main.route('/')
def index():
    '''
    Root page function 
    '''
    general_news = get_sources('general')
    print(general_news)
    return render_template('index.html', general=general_news)