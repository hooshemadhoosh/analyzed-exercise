import pandas as pd
import pickle
from os import listdir
import random
kind = {'A':"Cardio" , 'B' : 'Core' , 'C': 'Balance', 'D': 'Whole body' , 'E': 'Strengthing' , 'F': 'Stretching'}
level = ['Beginner','Intermediate','Advanced']
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
def get_exercise_names(dir0):
    print(dir0)
    file = pd.read_csv(dir0+'dictionary.csv',encoding='UTF-8')
    dictionary = {str(file['code'][i]):file['name'][i] for i in range(len(file['code']))}
    names = [name for name in listdir(dir0) if name.endswith('.jpg')]
    result = {key:[] for key in dictionary}
    for name in names:
        code = name.split('_')[0]
        try:
            result[code]+= [name]
        except:
            print("Name is not defined for a file...")
    result = {dictionary[key]:tuple(value) for key,value in result.items()}
    return result
dirs = {}
for key,value in kind.items():
    for lev in level:
        dirs[key+lev]=list(get_exercise_names(value+'\\'+lev+'\\').items())
def get_programs(bmi):
    result = []
    for i,pro in enumerate(program[bmi]):
        res = []
        for j in range(len(pro)//2):
            name_picture_pair = dirs[pro[2*j+1]+level[i]]
            
            res += [random.choices(name_picture_pair, k=int(pro[2*j]) )]
        result.append(res)
    return result



file = pd.read_excel('excel.xlsx',1)
data = {f"{file['gender'][i]} {file['name'][i]} {file['family'][i]}":{name:file[name][i] for name in file.columns} for i in range(len(file['BMI']))}
for key,value in data.items():
    value['BMI_VALUE'] = value['BMI']
    if value['BMI']<18.5:
        value['BMI']='Thin'
    elif 18.5<value['BMI']<25:
        value['BMI']='Normal'
    else:
        value['BMI']='Fat'
    data[key]=value
for key,value in data.items():
    temp = value
    temp['Program']=get_programs(value['BMI'])
    data[key]=temp



# import pprint
# pprint.PrettyPrinter(indent=4,width=30).pprint(dirs) 
# pprint.PrettyPrinter(indent=4,width=30).pprint(data)    
save_object(data,'data')