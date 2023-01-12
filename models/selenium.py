from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

class Selenium:
    BASE_URL = "https://web.whatsapp.com"
    BASE_MESSAGE_URL = "https://web.whatsapp.com/send?phone=+5212345678&text=HelloWorld"
    BASE_SELENIUM_SERVER = "http://localhost:4444/"

    def __init__(self):

        if(False):
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('--no-sandbox')
            self.options.add_argument("--disable-site-isolation-trials")
            self.options.add_argument("user-data-dir={}/config".format(os.getcwd()))
            self.driver = webdriver.Chrome(options=self.options)
    
    def test_open_browser(self):
        self.driver.get(Selenium.BASE_URL)

    def version(self):
        return 'v.0.1'