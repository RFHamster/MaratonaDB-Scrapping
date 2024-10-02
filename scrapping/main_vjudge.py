import requests
from bs4 import BeautifulSoup
import json

rootURL = "https://vjudge.net"

resposta = requests.get(rootURL + "/problem/CodeChef-EXUND")
print(resposta)

if(resposta.status_code == 200):
    soup = BeautifulSoup(resposta.content,'html.parser')
    iframe = (soup.find("iframe",{"id" : "frame-description"}))
    src = iframe["src"]
    response = requests.get(rootURL + src)

    iframe_soup = (BeautifulSoup(response.content,'html.parser'))
    #print(iframe_soup)

    # Extraindo o conteúdo da <textarea>
    textarea = iframe_soup.find("textarea", {"class": "data-json-container"})
    #print(textarea)
    json_content = textarea.string

    # Carregando o JSON
    data = json.loads(json_content)

    # Exibindo o conteúdo formatado
    for section in data['sections']:
        title = section['title']
        content = section['value']['content']
        
        print(f"Title: {title}")
        print(f"Content: {content}")
        print("="*40)
