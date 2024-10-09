from fpdf import FPDF
import re
import requests
import os
from PIL import Image
import io


# Docs
# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html


class PDF(FPDF):
    def __init__(self, titulo, origem, idOriginal):
        super().__init__()
        self.titulo = titulo
        self.origem = origem
        self.idOriginal = idOriginal
        self.set_title(titulo)
        self.set_author(origem)

    def header(self):
        self.set_font('Arial', 'B', 16)
        w = self.get_string_width(self.titulo) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, self.titulo, 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 9)
        self.set_text_color(128)
        bootom = self.origem + ' | ' + self.idOriginal
        self.cell(
            0, 10, bootom + ' - Página ' + str(self.page_no()), 0, 0, 'C'
        )

    def add_topic(self, titulo_topico: str):
        self.set_fill_color(255, 255, 255)
        self.set_font('Times', '', 14)
        self.cell(0, 6, titulo_topico, 0, 1, 'L', 1)

    def plot_teste(self):
        self.add_page()
        self.add_topic('Capitulo Teste')
        self.ln(4)
        txt = 'Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello '
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, txt)
        self.ln()

    def add_image_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            # with open('temp_image.jpg', 'wb') as f:
            #     f.write(response.content)
            # with Image.open('temp_image.jpg') as img:
            #     img_width, img_height = img.size

            img = Image.open(io.BytesIO(response.content))
            img_width, img_height = img.size

            img_width_mm = img_width * 0.264583
            img_height_mm = img_height * 0.264583

            x = (self.w - img_width_mm) / 2

            temp_image_path = 'temp_image.' + img.format.lower()
            img.save(temp_image_path)

            self.image(temp_image_path, x=x, y=self.get_y(), w=img_width_mm)
            self.ln(img_height_mm + 2)
            # Remove o arquivo temporário após uso
            os.remove(temp_image_path)

    def clean_text(self, text):
        text = re.sub(r'≤', '<=', text)
        text = re.sub(r'≥', '>=', text)
        text = re.sub(r'—', '-', text)
        return re.sub(r'[^\x00-\xFF]+', ' ', text)

    def write_descendant(self, tag):
        if tag.name is not None:
            if (
                tag.name == 'li'
                or tag.name == 'em'
                or tag.name == 'strong'
                or tag.name == 'tt'
                or tag.name == 'i'
            ):
                return False

            if tag.name == 'img':
                self.add_image_from_url(tag.get('src'))
            else:
                if tag.get_text() == '':
                    return False

                cleaned_text = self.clean_text(tag.get_text())
                if cleaned_text.strip():
                    self.multi_cell(0, 5, cleaned_text)
                    self.ln()
        return True

    def plot_pdf_scrapping_bee(self, soup_bee):
        self.add_page()
        self.set_font('Times', '', 12)

        for tag in soup_bee.find('div', class_='description').descendants:
            self.write_descendant(tag)

        self.add_topic('Entradas')
        self.ln(4)
        for tag in soup_bee.find('div', class_='input').descendants:
            self.write_descendant(tag)

        self.add_topic('Saidas')
        self.ln(4)
        for tag in soup_bee.find('div', class_='output').descendants:
            self.write_descendant(tag)

        div_both = soup_bee.find('div', class_='both')
        next_tables = div_both.find_all_next('table')

        self.add_topic('Exemplo(s)')
        self.multi_cell(
            0,
            5,
            '------------------------------------------------------------------------------------------------------------------',
        )
        for table in next_tables:
            tbody = table.find('tbody')
            tds = tbody.find_all('td')

            tdEntrada = tds[0]
            tdSaida = tds[1]

            self.add_topic('Exemplo de Entrada')
            self.ln(2)
            for desc in tdEntrada.find_all():
                self.write_descendant(desc)

            self.add_topic('Exemplo de Saida')
            self.ln(2)
            for desc in tdSaida.find_all():
                self.write_descendant(desc)

            self.multi_cell(
                0,
                5,
                '------------------------------------------------------------------------------------------------------------------',
            )

        self.ln()

    def write_descendant_cf(self, tag):
        if tag.name is not None:
            if (
                tag.name == 'li'
                or tag.name == 'em'
                or tag.name == 'strong'
                or tag.name == 'tt'
                or tag.name == 'i'
                or tag.name == 'span'
                or tag.name == 'nobr'
                or tag.name == 'script'
                or tag.name == 'mi'
                or tag.name == 'mo'
                or tag.name == 'math'
                or tag.name == 'msub'
                or tag.name == 'msup'
                or tag.name == 'mn'
            ):
                return False
            if tag.name == 'img':
                self.add_image_from_url(tag.get('src'))
            else:
                if tag.get_text() == '':
                    return False

                cleaned_text = self.clean_text(tag.get_text())
                if cleaned_text.strip():
                    self.multi_cell(0, 5, cleaned_text)
                    self.ln()
        return True

    def plot_pdf_scrapping_cf(self, soup_cf):
        self.add_page()
        self.set_font('Times', '', 12)

        for tag in (
            soup_cf.find('div', class_='input-specification')
            .find_previous_sibling('div')
            .descendants
        ):
            self.write_descendant_cf(tag)

        # self.add_topic('Entradas')
        # self.ln(4)
        for tag in soup_cf.find(
            'div', class_='input-specification'
        ).descendants:
            self.write_descendant_cf(tag)

        # self.add_topic('Saidas')
        # self.ln(4)
        for tag in soup_cf.find(
            'div', class_='output-specification'
        ).descendants:
            self.write_descendant_cf(tag)

        self.add_topic('Exemplo(s)')
        self.multi_cell(
            0,
            5,
            '------------------------------------------------------------------------------------------------------------------',
        )

        div_both = soup_cf.find('div', class_='sample-test')
        inputs = div_both.find_all_next('div', class_='input')
        outputs = div_both.find_all_next('div', class_='output')

        for i in range(len(inputs)):

            self.add_topic('Exemplo de Entrada')
            self.ln(2)
            for desc in inputs[i].find_all():
                if 'Copy' in desc.get_text() or desc.name == 'pre':
                    continue
                self.write_descendant_cf(desc)

            self.add_topic('Exemplo de Saida')
            self.ln(2)
            for desc in outputs[i].find_all():
                if 'Copy' in desc.get_text():
                    continue
                self.write_descendant_cf(desc)

            self.multi_cell(
                0,
                5,
                '------------------------------------------------------------------------------------------------------------------',
            )

        self.ln()
