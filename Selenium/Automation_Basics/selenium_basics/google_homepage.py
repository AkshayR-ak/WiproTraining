#code for Google homepage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#from selenium.webdriver.common.service import Service

browser = input('Enter which browser to use: ')
match (browser.lower()):
    case 'chrome':
        driver = webdriver.Chrome(service=Service('../resources/chromedriver.exe'))
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    case 'edge':
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
        #driver = webdriver.Chrome(service=Service(EdgeChromiumDriverManager().install()))
    case _:
        print('Unkown browser. So, using default Edge browser')
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

driver.get('https://google.com')

pagetitle = driver.title
if pagetitle == 'Google':
    print('Google Homepage loaded - pass')
else:
    print('Google Homepage not loaded - fail')
