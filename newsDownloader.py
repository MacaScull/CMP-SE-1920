import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=gb&'
       'apiKey=845600e6a98842b287f83a45af0479ed')
response = requests.get(url)
thenews = response.json()
articles = thenews["articles"]
i = 0
for a in articles:
    print (articles[i]["title"])
    print (articles[i]["description"])
    i +=1
