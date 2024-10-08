import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxService
import json
import random

origem = 'Beecrownd'

def make_scrapping(url: str):
    service = FirefoxService("/snap/bin/firefox.geckodriver")
    driver = Firefox(service=service)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        header = soup.find('div', class_='header')
        titulo = header.find('h1').text
        idOriginal = header.find('span').text.split(' ')[-1]
        dict(origem = origem, titulo = titulo, idOriginal = idOriginal)
        problema = soup.find('div', class_="problem")
        print(problema)
        driver.close()
        return dict
    except:
        driver.close()
        return dict()
    driver.close()


rootURL = 'https://www.beecrowd.com.br'
rootURL = rootURL + '/repository/UOJ_2047.html'
make_scrapping(rootURL)
