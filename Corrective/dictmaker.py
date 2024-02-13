import re
from os import walk,rename
from tkinter import filedialog

directory = filedialog.askdirectory()

def export_csv(datarows,filename):
    with open(filename,'w',encoding='UTF-8') as f: 
        f.write('\ufeff')
        for row in datarows:
            f.write((','.join(row)+'\n'))

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

if directory!='':
    counter = 0
    names = [('name','translation')]
    for dir_path, dir_names, file_names in walk(directory):
        new_file_names = []
        for name in file_names:
            new_name = name.replace(',','.')
            if ',' in name:
                rename(dir_path+'\\'+name,dir_path+'\\'+new_name)
                print(name,new_name)
                counter+=1
            new_file_names.append(new_name)
        for item in group_names(new_file_names):
            names.append((item[0],''))
    print(f'{counter} wrong name changed!')
    export_csv(names,'names.csv')
    print(f'{len(names)-1} filenames wrote to names.csv!')
    input()