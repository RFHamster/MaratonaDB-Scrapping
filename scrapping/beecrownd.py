import requests
from bs4 import BeautifulSoup
import json
import random

origem = "Beecrownd"

# lista com alguns UA's
user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
                   'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']

def make_scrapping(url: str):
    headers = {'User-Agent': random.choice(user_agent_list)}
    resposta = requests.get(url,headers=headers)

    titulo = ''        print(idOriginal)
    idOriginal = ''

    if(resposta.status_code == 200):
        soup = BeautifulSoup(resposta.content,'html.parser')
        header = soup.find('div', class_='header')
        titulo = header.find('h1').text
        idOriginal = header.find('span').text.split(" ")[-1]

rootURL = "https://www.beecrowd.com.br"
rootURL = rootURL + "/repository/UOJ_2023.html"
make_scrapping(rootURL)


