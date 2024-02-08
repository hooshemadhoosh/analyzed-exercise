import re
import random
from os import walk
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()

def group_names(name_list):
    names={}
    for name in name_list:
        mach = re.search(r'_\d+[.](jpg|png)',name)
        if mach==None:
            names[name[:-4]]=[name]
        else:
            try:
                names[name[:mach.span()[0]]].append(name)
            except:
                names[name[:mach.span()[0]]]=[name]
    return [(key,value) for key,value in names.items()]

def random_name_list(n,root):
    result = []
    folders = {}
    for dir_path, dir_names, file_names in walk(root):
        names = [i for i in file_names if i.endswith('.jpg') or i.endswith('.png')]
        if len(names):  folders[dir_path]=names
    names = list(folders.keys())
    ls = random.choices(names,weights=[len(group_names(folders[folder])) for folder in names],k=n) if len(names)<n else random.sample(names,k=n)
    for path in ls:
        result.append((path,random.choice(group_names(folders[path]))))
    return result
if directory!='':
    print(random_name_list(5,directory))