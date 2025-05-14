import requests 

url = "http://api.openweathermap.org/data/2.5/weather?q=London&appid=26631f0f41b95fb9f5ac0df9a8f43c92&units=metric"

def details(city, units='metric', api_key='26631f0f41b95fb9f5ac0df9a8f43c92'):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}" 
    res = requests.get(url)
    content = res.json()
    print(type(content)) 

    with open('../output_files/weathe.txt', 'a') as file: 
        for dict in content['list']: 
            info = f" {dict['dt_txt']}, {dict['main']['temp']}, {dict['weather'][0]['description']} \n"  
            print(info)
            file.write(info)


details('washington')