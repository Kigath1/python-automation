from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime as dt
import time

service = Service("chromedriver.exe")

def gettin_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=service, options=options) 
    driver.get("https://automated.pythonanywhere.com")
    return driver

# splitting the text to get the value of temperature
def split_text(text):
    splitted = float(text.split(": ")[1])
    return splitted

# function to create and write the file
def write_file(text):
    filename = f"temp_{dt.now().strftime("%m-%d.%H-%M-%S")}.txt"
    with open(filename, 'w') as file:
        file.write(text) 

def main(limit): 
    driver = gettin_driver()

    for _ in range(limit):
        time.sleep(2)
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        text = str(split_text(element.text))
        write_file(text)
        print(f"temperature recorded is {text} at {dt.now().strftime('%H:%M:%S')}")

    driver.quit()
    print("task successfull :) ")

main(5)




