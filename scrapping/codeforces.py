from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxService

origem = 'CodeForces'


def make_scrapping(url: str):
    # Only for Deb
    # service = FirefoxService('/snap/bin/firefox.geckodriver')
    # driver = Firefox(service=service)
    driver = Firefox()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()
    try:
        idOriginal = soup.title.string.replace(' ', '').split('-')[1]
        titulo = soup.find('div', class_='title').text
        origem = soup.find('th', class_='left').text + ' | CodeForces'
        problema = soup.find('div', class_='problemindexholder')
        return dict(
            titulo=titulo,
            idOriginal=idOriginal,
            problema=problema,
            origem=origem,
        )
    except:
        return dict()
