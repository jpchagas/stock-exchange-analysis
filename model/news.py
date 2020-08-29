class News():
    def __init__(self, news_source):
        self.source = news_source['source']['name']
        self.author = news_source['author']
        self.title = news_source['title']
        self.description = news_source['description']
        self.url = news_source['url']
        self.publishedAt = news_source['publishedAt']
        self.resume = news_source['content']
    '''
"source":{
         "id":"globo",
         "name":"Globo"
      },
      "author":"None",
      "title":"Petrobras inicia fase vinculante para venda da subsidiária Pbio",
      "description":"SÃO PAULO (Reuters) - A Petrobras iniciou nesta segunda-feira a fase não vinculante do processo de venda da subsidiária integral Petrobras Biocombustível (Pbio), informou a empresa em comunicado ao mercado.Fundada em...Leia mais",
      "url":"https://extra.globo.com/noticias/economia/petrobras-inicia-fase-vinculante-para-venda-da-subsidiaria-pbio-24564990.html",
      "urlToImage":"https://extra.globo.com/skins/extra/images/extra-face-1.jpg",
      "publishedAt":"2020-08-03T22:04:00Z",
      "content":"SÃO PAULO (Reuters) - A Petrobras iniciou nesta segunda-feira a fase não vinculante do processo de venda da subsidiária integral Petrobras Biocombustível (Pbio), informou a empresa em comunicado ao m… [+1120 chars]"
   },
    '''

    def getJson(self):
        json = {
            "source":self.source,
            "title":self.title,
            "resume":self.resume,
            "description":self.description,
            "url":self.url,
            "author":self.author,
            "publishedAt":self.publishedAt,
            
        }
        return json