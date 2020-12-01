# functional_tests.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException


# options = webdriver.ChromeOptions()
# browser = webdriver.Chrome(executable_path=r"C:\Windows\chromedriver_win32\chromedriver.exe", options=options)
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title