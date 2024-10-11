from scrapping import beecrownd, codeforces
from utils_pdf.pdf_generator import PDF
from fastapi import FastAPI, HTTPException, UploadFile, File, Body
from pydantic import BaseModel
import os
import requests
from constants import constants
from typing import Dict
import base64

# Url Teste Armazenamento
# 'https://codeforces.com/problemset/problem/2013/A'
# 'https://codeforces.com/problemset/problem/2008/B'
# 'https://www.beecrowd.com.br/repository/UOJ_1021.html'


class UrlRequest(BaseModel):
    url: str

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.post('/scrapping/beecrownd')
async def scrap_bee(request: UrlRequest) -> Dict:
    dicionario_bee = beecrownd.make_scrapping(request.url)
    if not dicionario_bee:
        raise HTTPException(
            status_code=404, detail='Data not found for the given URL'
        )

    pdf = PDF(
        dicionario_bee['titulo'],
        dicionario_bee['origem'],
        dicionario_bee['idOriginal'],
    )
    pdf.plot_pdf_scrapping_bee(dicionario_bee['problema'])
    pdf.output('bee.pdf', 'F')

    with open('bee.pdf', 'rb') as pdf_file:
        pdf_content = pdf_file.read()

    result = {
        'titulo': dicionario_bee['titulo'],
        'origem': dicionario_bee['origem'],
        'idOriginal': dicionario_bee['idOriginal'],
        'problema_pdf': base64.b64encode(pdf_content).decode('utf-8')
    }

    os.remove('bee.pdf')

    return result

    


@app.post('/scrapping/codeforces')
async def scrap_cf(request: UrlRequest) -> Dict:
    dicionario_cf = codeforces.make_scrapping(request.url)
    if not dicionario_cf:
        raise HTTPException(
            status_code=404, detail='Data not found for the given URL'
        )

    pdf = PDF(
        dicionario_cf['titulo'],
        dicionario_cf['origem'],
        dicionario_cf['idOriginal'],
    )
    pdf.plot_pdf_scrapping_cf(dicionario_cf['problema'])
    pdf.output('cf.pdf', 'F')

    with open('cf.pdf', 'rb') as pdf_file:
        pdf_content = pdf_file.read()

    result = {
        'titulo': dicionario_cf['titulo'],
        'origem': dicionario_cf['origem'],
        'idOriginal': dicionario_cf['idOriginal'],
        'problema_pdf': base64.b64encode(pdf_content).decode('utf-8')
    }

    os.remove('cf.pdf')

    return result
