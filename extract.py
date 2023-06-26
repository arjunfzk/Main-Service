from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    
    # prefs = {"profile.managed_default_content_settings.images":2}
    # chrome_options.headless = True


    #chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver

def getGoogleHomepage(driver: webdriver.Chrome) -> str:
    driver.get("https://www.google.com")
    return driver.page_source

def getCustomHomepage(driver: webdriver.Chrome,url) -> str:
    driver.get(url)
    print("sleeping")
    import time
    time.sleep(15)    
    scroll_amount = 400  # Adjust the value as per your requirements
    import time
    time.sleep(10)
    driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    print("done")
    return driver.page_source

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
