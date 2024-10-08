from scrapping import beecrownd
from utils_pdf.pdf_generator import PDF

rootURL = 'https://www.beecrowd.com.br'
rootURL = rootURL + '/repository/UOJ_1021.html'
dicionarioBee = beecrownd.make_scrapping(rootURL)

pdf = PDF(
    dicionarioBee['titulo'],
    dicionarioBee['origem'],
    dicionarioBee['idOriginal'],
)
pdf.plot_pdf_scrapping_bee(dicionarioBee['problema'])
pdf.output('tuto3.pdf', 'F')
