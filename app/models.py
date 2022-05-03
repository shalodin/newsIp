class Sources:
    '''
    
    sources class to define news sources objects

    '''
    def __init__(self,id,name,description,url,category,country):
        self.id = id
        self.name = name
        self.description=description
        self.url=url
        self.category=category
        self.country=country


class Articles:
    '''
    Articles class to define articles objects

    '''
    def __init__(self,id,author,title,description,url,urlToImage,publishedAt):
        self.id = id
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt

