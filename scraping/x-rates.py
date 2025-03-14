from bs4 import BeautifulSoup
import requests 

def get_currency(curr_in, curr_out):
    url = f'https://www.x-rates.com/calculator/?from={curr_in}&to={curr_out}&amount=1'
    content = requests.get(url).text 
    # print(content) 

     # printing the html contents to a html and a txt file for the case where you cannot access the source code
    """
    txt_file = 'output_files/out_file.txt'
    html_file = 'output_files/out_file.html'
    with open (html_file, 'w', encoding="utf-8") as code_in_file:
        code_in_file.write(content) 
    """

    soup = BeautifulSoup(content, 'html.parser')
    curr_rate = soup.find("span", class_="ccOutputRslt").text 
    curr_rate = float(curr_rate[:-4])
    # print(curr_rate)

    return curr_rate

print(get_currency('USD', 'EUR'))
print(get_currency('EUR', 'INR'))


