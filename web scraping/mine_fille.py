from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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

def split_text(text):
    splitted = float(text.split(": ")[1])
    return splitted

def main(limit): 
    driver = gettin_driver()
    # time.sleep(2)
    
    count = 0 
    while count < limit: 
        time.sleep(2)
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        temp = split_text(element.text)
        try:
            if temp is not None:
                file = f"temp_{int(time.time())}.txt"
                with open(file, "w") as file:
                    file.write(str(temp))
                    print(f"Saved temperature {temp} to {file.name}")  # Use file.name to print filename
            else: 
                print("No temperature found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        count += 1  # Increment the counter
        time.sleep(1)  # Wait before the next iteration


def mai(limit): 
    driver = gettin_driver()
    time.sleep(2)
    
    count = 0 
    while count < limit: 
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        temp = split_text(element.text)
        try:
            if temp is not None:
                file = f"temp_{int(time.time())}.txt"
                with open(file, "w") as file:
                    file.write(str(temp))
                    print(f"saved temparuter {temp} to {file}")
            else: 
                print("No temperature found.")
        except Exception as e:
            print(f"An error occurred : {e}")
        
        time.sleep(1)
    
def other_main():   
    driver = gettin_driver()
    time.sleep(2)

    count = 0
    while count < 11:
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        temp = split_text(element.text)
        print(temp)
        count += 1
        time.sleep(2)

# other_main()
main(limit=3)



