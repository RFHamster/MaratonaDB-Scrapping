import requests
from bs4 import BeautifulSoup
import json
import random

# lista com alguns UA's
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
]

# escolhendo aleatoriamente um UA
user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}

rootURL = 'https://codeforces.com'

resposta = requests.get(
    rootURL + '/problemset/problem/2004/G', headers=headers
)
print(resposta)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.content, 'html.parser')
    print(soup)
