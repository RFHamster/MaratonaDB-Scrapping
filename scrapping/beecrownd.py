from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxService

origem = 'Beecrownd'


def make_scrapping(url: str):
    # Only for Deb
    # service = FirefoxService('/snap/bin/firefox.geckodriver')
    # driver = Firefox(service=service)
    driver = Firefox()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()
    try:
        header = soup.find('div', class_='header')
        titulo = header.find('h1').text
        idOriginal = header.find('span').text.split(' ')[-1]
        problema = soup.find('div', class_='problem')

        return dict(
            titulo=titulo,
            idOriginal=idOriginal,
            problema=problema,
            origem=origem,
        )
    except:
        return dict()
