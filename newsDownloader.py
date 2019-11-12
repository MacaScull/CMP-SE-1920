import requests

class news:
       def __init__(self):
              self.newsData = []

       def getNews(self):
              url = ('https://newsapi.org/v2/top-headlines?'
                     'country=gb&'
                     'apiKey=845600e6a98842b287f83a45af0479ed')
              response = requests.get(url)
              thenews = response.json()
              articles = thenews["articles"]
              i = 0
              for a in articles:
              #print (articles[i]["title"])
                     self.newsData.append(str(articles[i]["title"]) + " " + str(articles[i]["description"]))
              #print (articles[i]["description"])
                     i +=1

#----Test-----
#a = news()
#a.getNews()
#print (a.newsData[0])