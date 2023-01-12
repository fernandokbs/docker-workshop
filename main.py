from models import selenium
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    driver = selenium.Selenium()
    print(driver.version())
    driver.test_open_browser()

    return "<p>Docker workshop 2022!</p>"