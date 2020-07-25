
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='376aca59ef1c4bfe9ec2dcc7b9c53231')

fontes = []
# /v2/sources
getsources = newsapi.get_sources(country='br')
for s in getsources['sources']:
    fontes.append(s['name'])

#print(fontes)

#/v2/everything
all_articles = newsapi.get_everything(q='Petrobras',
                                      sources='Blasting News (BR)','Globo', 'Google News (Brasil)', 'InfoMoney',
                                      from_param='2020-06-01',
                                      to='2020-07-01',
                                      sort_by='relevancy',
                                      #page=2)
                                        )

print(all_articles['totalResults'])
print(all_articles['articles'])