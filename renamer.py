from os import listdir,rename
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

directory = filedialog.askdirectory()
print (directory)

result = '\ufeff'
result += 'code,name\n'

paths = [name for name in listdir(directory) if name.endswith('.jpg')]
data = {key.split('_')[0]:[] for key in paths}
for path in paths:
    data[path.split('_')[0]]+=[directory+'/'+path]

for i,dic in enumerate(data.items()):
    result+= f"{i+1},{dic[0]}\n"
    for path in dic[1]:
        newpath = path.replace(dic[0],str(i+1))
        # print(path,newpath)
        rename(path,newpath)
with open(directory+'/dictionary.csv','w',encoding='UTF-8') as f:
    f.write(result)
print(result)