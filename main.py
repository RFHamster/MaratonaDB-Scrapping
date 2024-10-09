from scrapping import beecrownd, codeforces
from utils_pdf.pdf_generator import PDF
from fastapi import FastAPI
from pydantic import BaseModel

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
async def root(request: UrlRequest):
    dicionario_bee = beecrownd.make_scrapping(request.url)

    pdf = PDF(
        dicionario_bee['titulo'],
        dicionario_bee['origem'],
        dicionario_bee['idOriginal'],
    )
    pdf.plot_pdf_scrapping_bee(dicionario_bee['problema'])
    pdf.output('bee.pdf', 'F')


@app.post('/scrapping/codeforces')
async def root(request: UrlRequest):
    dicionario_cf = codeforces.make_scrapping(request.url)
    pdf = PDF(
        dicionario_cf['titulo'],
        dicionario_cf['origem'],
        dicionario_cf['idOriginal'],
    )
    pdf.plot_pdf_scrapping_cf(dicionario_cf['problema'])
    pdf.output('cf.pdf', 'F')
