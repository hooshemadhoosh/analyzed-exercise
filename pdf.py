#Add C:\Program Files (x86)\Google\Chrome\Application to PATH Environment Variable then run the program
from subprocess import Popen,PIPE
from os import listdir
import tkinter as tk
from tkinter import filedialog
import os
def html_to_pdf(html_file_name,pdf_file_name):
    command = f"chrome --headless --disable-gpu --print-to-pdf={pdf_file_name} --no-pdf-header-footer --run-all-compositor-stages-before-draw --no-margins --no-sandbox {html_file_name}"
    process = Popen(command.split(), stdout=PIPE, stderr=PIPE,shell=True)
    process.communicate()
    print(f"PDF Created as {pdf_file_name}")

def html_to_pdf2(html_file_name,pdf_file_name):
    command = f"wkhtmltopdf --margin-top 0 --margin-bottom 0 --margin-left 0 --margin-right 0 --background --print-media-type --enable-smart-shrinking --page-size Letter --encoding UTF-8 {html_file_name} {pdf_file_name}"
    process = Popen(command.split(), stdout=PIPE, stderr=PIPE,shell=True)
    process.communicate()
    print(f"PDF Created as {pdf_file_name}")

root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()+'/'
result_folder = 'PDF_Files/'
if directory!="":
    if not os.path.exists(directory+result_folder):  os.mkdir(directory+result_folder)
    names = [name for name in listdir(directory) if name.endswith('.html')]
    for name in names:
        html_to_pdf(directory+name,directory+result_folder+name.replace('.html','.pdf'))
