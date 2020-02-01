import urllib.request,json
from .models import Sources


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
    