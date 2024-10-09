from scrapping import beecrownd, codeforces
from utils_pdf.pdf_generator import PDF

# rootURL = 'https://www.beecrowd.com.br'
# rootURL = rootURL + '/repository/UOJ_1021.html'
# dicionarioBee = beecrownd.make_scrapping(rootURL)
#
# pdf = PDF(
#     dicionarioBee['titulo'],
#     dicionarioBee['origem'],
#     dicionarioBee['idOriginal'],
# )
# pdf.plot_pdf_scrapping_bee(dicionarioBee['problema'])
# pdf.output('tuto3.pdf', 'F')

rootUrl = 'https://codeforces.com/problemset/problem/2013/A'
dicionarioCF = codeforces.make_scrapping(rootUrl)
pdf = PDF(
    dicionarioCF['titulo'],
    dicionarioCF['origem'],
    dicionarioCF['idOriginal'],
)
pdf.plot_pdf_scrapping_cf(dicionarioCF['problema'])
pdf.output('tuto3.pdf', 'F')
