# in this file we are going to use the newsapi.org API to get the latest news articles related to a specific topic and save them to a text file.
import requests

def url_details(topic, from_date, to_date, api_key='890603a55bfa47048e4490069ebee18c'): 
    url=f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language=en&apiKey={api_key}'

    results = requests.get(url)
    content = results.json()
    articles = content.get('articles',[])
    results = []

    for article in articles: 
        results.append(f"TITLE\n{article['title']}\nDESCRIPTION\n{article['description']}\n")

    return results

article_results = url_details('stock market', '2025-04-27', '2025-04-28')
for entry in article_results:
    print(entry)

filename = "../output_files/stock_market.txt"
with open(filename, 'w', encoding='utf-8') as file: 
    for entry in article_results:
        file.write(entry + "\n")

