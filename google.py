from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def google_this(x="Dogs"):
    browser = webdriver.Chrome()
    browser.get('https://www.google.com/')
    search = browser.find_element_by_name('q')

    search.send_keys(x)
    search.send_keys(Keys.RETURN)

    return browser

var = google_this('cats')
