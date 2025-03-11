from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

service = Service("chromedriver.exe")

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("no-sandbox")
    # options.add_argument("headless")
    options.add_argument("disable-dev-shm-usage") 
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://titan22.com/account/login")
    return driver

def main():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)  # Explicit wait
    
    # Fill in login details
    driver.find_element(By.ID, "CustomerEmail").send_keys("willalbert2029@gmail.com")
    driver.find_element(By.ID, "CustomerPassword").send_keys("pass1234word" + Keys.RETURN)
    print("Operation successful")

    # Wait for page to load completely before clicking the footer link
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a")))
        element.click()
        print("Second operation good")

        time.sleep(2)
        print(driver.current_url)
    except:
        print("Element not found. Check if the XPath is correct or if it's inside an iframe.")

main()
