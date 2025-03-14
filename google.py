
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time

service = Service(executable_path="scraping/chromedriver.exe")
def get_driver():  
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized") 
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")  
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_argument("--log-level=3")  # Suppress logs
    options.add_argument("--headless")  # Run in headless mode
    # options.add_argument("--disable-gpu")  # Disable GPU acceleration

    driver = webdriver.Chrome(service=service)

    driver.get("https://google.com")
    time.sleep(3)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Nothing phone" + Keys.RETURN) 

    time.sleep(30)
    driver.quit()

get_driver()


