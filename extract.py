
import undetected_chromedriver as uc  # Note import before selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyvirtualdisplay

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'


def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f'user-agent={user_agent}')

    # prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True


    #chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver

def getGoogleHomepage(driver: webdriver.Chrome) -> str:

    
    with pyvirtualdisplay.Display(visible=0, size=(800, 600)) as _:
        import time
        time.sleep(15)    
        driver.get("https://www.msn.com/en-us/news/technology/wingpt-is-a-new-chatgpt-app-for-your-ancient-windows-31-pc/ar-AA1d2RZR")
        time.sleep(10)
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
