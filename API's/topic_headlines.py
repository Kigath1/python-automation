# uses same code as the one on the news api file but with a little change to the url_details
import requests

# url= https://newsapi.org/v2/top-headlines?country=us&apiKey=890603a55bfa47048e4490069ebee18c

def url_details(country, api_key='890603a55bfa47048e4490069ebee18c'): 
    url=f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'

    results = requests.get(url)
    content = results.json()
    articles = content.get('articles',[])
    results = []

    for article in articles: 
        results.append(f"TITLE\n{article['title']}\nDESCRIPTION\n{article['description']}\n")

    return results

article_results = url_details('us')
for entry in article_results:
    print(entry)

# you can choose to print the results or save them to a file
# filename = "../output_files/stock_market.txt"
# with open(filename, 'w', encoding='utf-8') as file: 
#     for entry in article_results:
#         file.write(entry + "\n")

