import pdfkit 
from os import listdir
files = listdir('./sport-program-build')
addr = r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=addr)
options = {
    'page-size': 'A4',
    'margin-top': '0in',
    'margin-right': '0in',
    'margin-bottom': '0in',
    'margin-left': '0in',
    'orientation':'portrait',
    # 'encoding': "UTF-8",
    # 'custom-header': [
    #     ('Accept-Encoding', 'gzip')
    # ],
    # 'cookie': [
    #     ('cookie-empty-value', '""'),
    #     ('cookie-name1', 'cookie-value1'),
    #     ('cookie-name2', 'cookie-value2'),
    # ],
    'no-outline': None
}
for i in files:
    pdfkit.from_file( f'./sport-program-build/{i}', f'{i[:-5]}.pdf' ,configuration=config , options=options)
