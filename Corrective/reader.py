import re
import pandas as pd
import pickle
from os import walk
import random

from sympy import true
# 24=>49
# 50=>87
translate= {}
root = "Corrective"
kind = {'M':"1-Inhibit" , 'N' : '2-Lengthen' , 'O': '3-Activation', 'P': '4-Integrated'}
level = {'Beginner':0,'Intermediate':1,'Advanced':2}
person_level = {'1':('Beginner' , 'Beginner') ,
                 '4' : ('Beginner' , 'Intermediate' , 'Advanced' , 'Advanced'),
                   '3' : ('Beginner' , 'Intermediate' , 'Intermediate') ,
                     '2':('Beginner' , 'Intermediate' , 'Intermediate') ,
                'false':('Beginner' , 'Intermediate' , 'Intermediate'),
                '':('Beginner' , 'Intermediate' , 'Intermediate'),
                  '5':('Intermediate' , 'Intermediate' , 'Advanced' , 'Advanced')}
program = ['1M3N3O1P','2M4N4O2P','3M5N5O3P']

def merge_dict(a,b):
    for key,value in b.items():
        a[key]=value
    return a

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


def save_object(obj,filename):
    try:
        with open(filename, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
def get_exercise_names(dir0):
    # file = pd.read_csv(dir0+'dictionary.csv',encoding='UTF-8')
    # dictionary = {str(file['code'][i]):file['name'][i] for i in range(len(file['code']))}
    pass

def suitable_exercises(static,dynamic,n):
    res = []
    for item in static:
        if item[1]==5 or n==0:  break
        res.append(item[0])
        n-=1
    for item in dynamic:
        if n==0:  break
        res.append(item[0])
        n-=1
    return res

def get_programs(static,dynamic,pers_level): #[[(,),(,),...],[(,),(,),...],[(,),(,),...],...]
    result = []
    exer = suitable_exercises(static,dynamic,len(person_level[pers_level]))
    for i,lev in enumerate(person_level[pers_level]):
        res = []
        pro = program[level[lev]]
        for j in range(len(pro)//2):
            res.append(random_name_list(int(pro[2*j]),f'{root}\\{translate[exer[i]]}\\{kind[pro[2*j+1]]}'))
        result.append(res)
    return result



file = pd.read_excel('excel.xlsx',0,dtype='str',keep_default_na= False)

data = {f"{file['gender'][i]} {file['name'][i]} {file['family'][i]}":merge_dict({name:file[name][i] for name in file.columns},{"STATIC":sorted(tuple(file.iloc[i,24:50].items()),key=lambda x:x[1]),"DYNAMIC":sorted(tuple(file.iloc[i,50:88].items()),key=lambda x:x[1],reverse=True)}) for i in range(len(file['name']))}

for key,value in data.items():
    temp = value
    temp['Program']=get_programs(value['STATIC'],value['DYNAMIC'],str(value['PERSON_LEVEL']))
    data[key]=temp



# import pprint
# pprint.PrettyPrinter(indent=4,width=30).pprint(dirs) 
# pprint.PrettyPrinter(indent=4,width=30).pprint(data)    
# save_object(data,'data')