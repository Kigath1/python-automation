from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time 

service = Service("chromedriver.exe")

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("no-sandbox")
    # options.add_argument("headless")
    options.add_argument("disable-dev-smh-usage")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://titan22.com/account/login")
    return driver

def main():
    driver = get_driver()
    driver.find_element(by="id", value="CustomerEmail").send_keys("willalbert2029@gmail.com")
    driver.find_element(by="id", value="CustomerPassword").send_keys("pass1234word" + Keys.RETURN)
    print("operation successfull")
    time.sleep(5)
    driver.find_element(by="xpath", value=('//*[@id="shopify-section-footer"]/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a')).click()
    print("second op good")
    time.sleep(2)
    print(driver.current_url)

main()  