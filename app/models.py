class Sources:
    def __init__(self, news_id, name, description,url,category, language, country):
        self.news_id = news_id
        self.name = name
        self.description = description
        self.url = url 
        self.category = category
        self.language = language
        self.country = country
        

class Articles:
    def __init__(self, author, title, description, article_url, image_url, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.article_url = article_url 
        self.image_url = image_url
        self.publishedAt = publishedAt
    
        