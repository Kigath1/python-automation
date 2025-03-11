
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# without using the path where the file is installed us this then modify calling this
# from webdriver_manager.chrome import ChromeDriverManager 

# service = Service('C:\\Users\\Dennis\\Desktop\\python\\udemy\\web scraping\\chromedriver.exe')
# if you have the driver in the current folder no need to write the whole path, 
service = Service("chromedriver.exe")

def get_driver():
    #set the options to make browsing easier 
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_argument("--log-level=3")  # Suppress logs

    driver = webdriver.Chrome(service=service, options=options)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) # this is where you modify
    driver.get("https://automated.pythonanywhere.com")
    return driver


def clean_text(text):
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text) 

print(main())  







def mainer():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text 

print(mainer()) 


"""
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.google.com")
print(driver.title)

driver.quit()
"""


