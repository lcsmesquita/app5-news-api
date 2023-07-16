import requests
from send_email import send_email

topic = "tesla"

api_key = "56f2115a07484add8b19537abb98a47c"

# API que retorna informações sobre a tesla.
url = "https://newsapi.org/v2/everything?" \
        f"q={topic}&" \
        "from=2023-06-16&" \
        "sortBy=publishedAt&apiKey=" \
        "56f2115a07484add8b19537abb98a47c&" \
        "language=en"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json() #using information as a dictionary

# Acess the article titles and description
body = "Subject: Today's news" + "\n"
for article in content['articles'][0:20]:
    if article["title"] is not None:
        body = body + article['title'] + "\n" \
            + article["description"] + "\n" \
                + article['url'] + 2*"\n"

body = body.encode('utf-8')
send_email(message=body)