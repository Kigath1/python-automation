from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time 

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
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver


def split_text(text):
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver() 
    driver.find_element(by="id", value="id_username").send_keys("automated") 
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN) 
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(5)
    print(driver.current_url)

    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    element2 = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")

    print(element.text)
    print(split_text(element2.text)) 

main() 


