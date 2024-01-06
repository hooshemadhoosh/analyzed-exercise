# #import asyncio
# from pyppeteer import launch
from os import listdir

# async def generate_pdf_from_html(html_content, pdf_path):
#     browser = await launch()
#     page = await browser.newPage()
    
#     await page.setContent(html_content)
    
#     await page.pdf({'path': pdf_path, 'format': 'A4'})
    
#     await browser.close()

# for i in listdir('./'):
#     if i != 'index.html' and i[-4:] == 'html':
#         htmlfile = open(f'sport-program-build/{i}' , 'r' , encoding='utf8')
#         index = htmlfile.read()
#         if __name__ == '__main__':
#             loop = asyncio.new_event_loop()
#             asyncio.set_event_loop(loop)
#             try:
#                 asyncio.get_event_loop().run_until_complete(generate_pdf_from_html(index, 'index.pdf'))    
#             except KeyboardInterrupt:
#                 pass


# # HTML content
# # Run the function


from xhtml2pdf import pisa

def convert_html_to_pdf(html_string, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)
        
    return not pisa_status.err

files = listdir('./')
print (files)
for fi in files:
    if fi != 'index.html' and fi[-4:] == 'html':
        html_content = open(f'{fi}' , 'r' , encoding='utf8')
        html_content = html_content.read()
        if convert_html_to_pdf(html_content, f'./{fi}'):
            print(f"PDF generated and saved at {fi}")
        else:
            print("PDF generation failed")