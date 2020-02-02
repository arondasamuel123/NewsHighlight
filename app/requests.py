import urllib.request,json
from .models import Sources,Articles



api_key = 'None'

base_url = 'None'


def configure_request(app):
    global api_key, base_url
    api_key = app.config['API_KEY']
    base_url = app.config['SOURCE_API_URL']
   
    

def get_sources(category):
    """
    Function to get response from api endpoint 
    """
    get_sources_url = base_url.format(category, api_key)
    print(get_sources_url)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        # print(get_sources_response['sources'])
        sources_results = None
        
        
        if get_sources_response['sources']:
            sources_response_list = get_sources_response['sources']
            sources_results = process_sources(sources_response_list)
            
    return sources_results

def process_sources(source_response_list):
    """
    Function to process the response from the endpoint and convert it to an object
    """
    sources_results = []
    for source_item in source_response_list:
        news_id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        
        
        if url: 
            source_object = Sources(news_id, name, description,url,category,language,country)
            sources_results.append(source_object)
            # print(sources_results)
    return sources_results


def get_articles(news_id):
    get_article_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(news_id, api_key)
    print(get_article_url)
    with urllib.request.urlopen(get_article_url) as url:
        response_data = url.read()
        # print(response_data)
        response = json.loads(response_data)
        
        articles = None
        
        if response['articles']:
            articles_response_list = response['articles']
            # print(articles_response_list)
            
            
    return articles_response_list

# def process_response(articles_response_list):
    
#     articles = []
#     for article_item in articles_response_list:
#         author = article_item.get('author')
#         title = article_item.get('title')
#         description = article_item.get('description')
#         article_url = article_item.get('url')
#         image_url = article_item.get('urlToImage')
#         publishedAt = article_item.get('publishedAt')
        
#         if image_url:
#             articles_object = Articles(author, title, description, article_url, image_url, publishedAt)
#             articles.append(articles_object)
#             # print(type(articles))
#     return articles_object
             
    
            

        
        
        
            
    