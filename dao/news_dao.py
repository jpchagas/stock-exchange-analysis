from newsapi import NewsApiClient
from model.news import News
import json

class NewsDAO():
  def __init__(self):
    self.newsapi = NewsApiClient(api_key='376aca59ef1c4bfe9ec2dcc7b9c53231')
    

  def create_news(self,json_news):
    news_list = []
    for news in json_news:
      news_list.append(News(news))
    return news_list

  def getNews(self,word,begin,end):
    #/v2/everything
    all_articles = self.newsapi.get_everything(q=word,
                                        sources='Blasting News (BR),Globo, Google News (Brasil), InfoMoney',
                                        from_param=begin,
                                        to=end,
                                        sort_by='relevancy',
                                        #page=2)
                                          )
    return all_articles['articles']
  
  def getSources(self):
    fontes = []
    # /v2/sources
    getsources = self.newsapi.get_sources(country='br')
    for s in getsources['sources']:
        fontes.append(s['name'])

    return fontes

  def getJsonList(self,news_list):
    news_list_formated = []
    for news in news_list:
      news_list_formated.append(news.getJson())
    return news_list_formated