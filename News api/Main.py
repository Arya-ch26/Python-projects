import requests

query=input("What type of news are you intrested in today?\n")
api="2c36019729534613a6b92de45f70db77"

url=f"https://newsapi.org/v2/everything?q={query}&apiKey={api}"

print(url)
r=requests.get(url)
data=r.json()
articles=data["articles"]

for index, article in enumerate(articles):
    print(f"{index+1}. {article['title']}\n🔗 {article['url']}")

    print("\n**************\n")