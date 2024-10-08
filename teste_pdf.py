from fpdf import FPDF

# Docs
# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html

class PDF(FPDF):
    def __init__(self, titulo, origem, idOriginal):
        super().__init__()
        self.titulo = titulo
        self.origem = origem
        self.idOriginal = idOriginal

    def header(self):
        self.set_font('Arial', 'B', 16)
        w = self.get_string_width(self.titulo) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, self.titulo, 0, 1, 'C')
        self.ln(5)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 9)
        # Text color in gray
        self.set_text_color(128)
        bootom = self.origem + " | " + self.idOriginal
        # Page number
        self.cell(0, 10, bootom + " - Página " +  str(self.page_no()), 0, 0, 'C')

    def add_topic(self, titulo_topico: str):
        self.set_fill_color(255, 255, 255)
        self.set_font('Times', '', 14)
        self.cell(0, 6, titulo_topico, 0, 1, 'L', 1)

    def plot_teste(self):
        self.add_page()
        # Arial 12
        self.add_topic("Capitulo Teste")
        # Line break
        self.ln(4)
        # Read text file
        txt = 'Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello '
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        self.ln()
        self.multi_cell(0, 5, txt)
        self.ln()
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()

    def plot_pdf_scrapping(self):
        self.add_page()
        self.add_topic("Capitulo Teste")
        # Line break
        self.ln(4)
        # Read text file
        txt = 'Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello '
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        self.ln()
        self.multi_cell(0, 5, txt)

        # Line break
        self.ln()

pdf = PDF("Titulo", "Beecrownd", "2023")
pdf.plot_pdf_scrapping()
pdf.set_title(title)
pdf.set_author('Jules Verne')
pdf.output('tuto3.pdf', 'F')