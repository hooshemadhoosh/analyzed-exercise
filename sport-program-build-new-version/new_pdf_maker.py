#import asyncio
#from pyppeteer import launch
import os
#async def generate_pdf_from_html(html_content, pdf_path):
#    browser = await launch()
#    page = await browser.newPage()
#    
#    await page.setContent(html_content)
#    
#    await page.pdf({'path': pdf_path, 'format': 'A4'})
#    
#    await browser.close()
#
## Run the function
#for files in os.listdir('./'):
#    if files != 'index.html' and files[-4:] == 'html':
#        htmlfile = open(f'./{files}' , 'r' , encoding='utf-8')
#        htmlfile = htmlfile.read()
#        print (type(htmlfile))
#        asyncio.get_event_loop().run_until_complete(generate_pdf_from_html(htmlfile, f'{files[:-5]}.pdf'))
#

from xhtml2pdf import pisa

def convert_html_to_pdf(html_string, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)
    return not pisa_status.err

for files in os.listdir('./'):
    if files != 'index.html' and files[-4:] == 'html':
        htmlfile = open(f'./{files}' , 'r' , encoding='utf-8')
        html_content = htmlfile.read()
# Generate PDF
        if convert_html_to_pdf(html_content, f'{files[:-5]}.pdf'):
            print(f"PDF generated")
        else:
            print("PDF generation failed")