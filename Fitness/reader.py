from math import nan
import re
import pandas as pd
import pickle
from os import listdir
import random

root = "Fitness_Backup\\"
kind = {'A':"Cardio" , 'B' : 'Core' , 'C': 'Balance', 'D': 'Whole body' , 'E': 'Strengthing' , 'F': 'Stretching'}
level = {'Beginner':0,'Intermediate':1,'Advanced':2}
person_level = {'بی تحرک':('Beginner' , 'Beginner') ,
                 'بسیار فعال' : ('Beginner' , 'Intermediate' , 'Advanced' , 'Advanced'),
                   'نسبتا فعال' : ('Beginner' , 'Intermediate' , 'Intermediate') ,
                     'کم تحرک':('Beginner' , 'Intermediate' , 'Intermediate') ,
                'false':('Beginner' , 'Intermediate' , 'Intermediate'),
                nan:('Beginner' , 'Intermediate' , 'Intermediate'),
                  'بیش از حد فعال':('Intermediate' , 'Intermediate' , 'Advanced' , 'Advanced')}
program = {"Thin":['1A1B1C1D3E1F','2A2B1C1D4E2F','3A3B1C1D5E3F'],
           "Fat":['3A1B1C1D1E1F','5A1B1C1D2E2F','7A2B1C1D2E3F'],
           "Normal":['2A1B1C1D2E1F','3A2B1C1D3E2F','4A2B2C1D4E3F']}
#program = {"Thin":['1A','2A','3A'],
#           "Fat":['3A2A','5A1A','7A3A'],
#           "Normal":['2A3A','3A1A','4A2A']}
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

file = pd.read_csv('Fitness.csv',encoding='UTF-8')
dictionary = {str(file['name'][i]):file['translation'][i] for i in range(len(file['name']))}
def get_exercise_names(dir0):
    print(dir0)
    # dictionary = load_object('FitnessNamesObject')
    names = [name for name in listdir(dir0) if name.endswith('.jpg')]
    result = {key:[] for key in dictionary}
    for name in names:
        mach = re.search(r'_\d+[.](jpg|png)',name)
        if mach==None:
            code=name[:-4]
        else:
            code = name.split('_')[0]
        try:
            result[dictionary[code]]+= [dir0+name]
        except:
            print(f"Name is not defined for file {name}")
            dictionary[code]=code
            result[code]=[dir0+name]
    result = {dictionary[key]:tuple(value) for key,value in result.items() if value!=[]}
    return result
dirs = {}
for key,value in kind.items():
    for lev in level:
        dirs[key+lev]=list(get_exercise_names(root+value+'\\'+lev+'\\').items())
        print(key+lev,dirs[key+lev])
def get_programs(bmi,pers_level): #[[(,),(,),...],[(,),(,),...],[(,),(,),...],...]
    result = []
    for lev in person_level[pers_level]:
        res = []
        pro = program[bmi][level[lev]]
        for j in range(len(pro)//2):
            name_picture_pair = dirs[pro[2*j+1]+lev]
            
            res += [random.choices(name_picture_pair, k=int(pro[2*j]) )]
        result.append(res)
    return result



file = pd.read_excel('excel.xlsx',1,dtype='str',keep_default_na= False)

data = {f"{file['gender'][i]} {file['name'][i]} {file['family'][i]}":{name:file[name][i] for name in file.columns} for i in range(len(file['BMI']))}
for key,value in data.items():
    value['BMI_VALUE'] = value['BMI']
    value['BMI'] = float(value['BMI'])
    if value['BMI']<18.5:
        value['BMI']='Thin'
    elif 18.5<value['BMI']<25:
        value['BMI']='Normal'
    else:
        value['BMI']='Fat'
    data[key]=value
for key,value in data.items():
    temp = value
    temp['Program']=get_programs(value['BMI'],value['PERSON_LEVEL'].lower())
    data[key]=temp



# import pprint
# pprint.PrettyPrinter(indent=4,width=30).pprint(dirs) 
# pprint.PrettyPrinter(indent=4,width=30).pprint(data)    
save_object(data,'data')
input("******Done******")