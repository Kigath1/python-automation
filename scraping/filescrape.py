from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service("chromedriver.exe")


def get_driver():
    # Set the options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_argument("--log-level=3")  # Suppress logs

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com/")  # Directly visit the page without login
    return driver


def split_text(text):
    splitted = float(text.split(": ")[1])
    return splitted

def main():
    driver = get_driver()
    while True:
        try:
            element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
            temperature = split_text(element.text)
            if temperature is not None:
                filename = f"temperature_{int(time.time())}.txt"
                with open(filename, "w") as file:
                    file.write(str(temperature))
                    print(f"Saved temperature {temperature} to {filename}")
            else:
                print("No valid temperature found.")
        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(2)  # Wait for 2 seconds before scraping again


if __name__ == "__main__":
    main()
