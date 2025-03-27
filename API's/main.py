import requests 
import json 

url = 'https://newsapi.org/v2/everything?qInTitle=united%20states&from=2025-2-27&to=2025-2-28&sortBy=popularity&language=en&apiKey=49e3cc5576ec4c26bcf157ee45e712cc'

content = requests.get(url).json()
print(content)
# print(content["articles"][0]["content"])

# f_content = json.dumps(content, indent=4)
# print(f_content)

# txt_file = '../output_files/news.txt'
# with open (txt_file, 'w') as code_in_file:
#     code_in_file.write(f_content) 

