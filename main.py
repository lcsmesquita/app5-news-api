import requests

api_key = "56f2115a07484add8b19537abb98a47c"

# API que retorna informações sobre a tesla.
url = "https://newsapi.org/v2/everything?q=tesla" \
    "&from=2023-06-16&sortBy=publishedAt&apiKey=" \
        "56f2115a07484add8b19537abb98a47c"

request = requests.get(url)
content = request.json() #using information as a dictionary

for article in content['articles']:
    print(article['title'])