import re
import pandas as pd
import pickle
from os import walk
import random

from sympy import true
# 24=>49
# 50=>87
translate= {'سر به جلو': 'Forward Head', 'شانه گرد': 'Rounded Shoulder', 'پشت گرد': 'hyper Kyphosis', 'پشت تابدار': 'Swayback', 'برآمدگی شکم': 'Abdomen Protruding', 'کمر گود': 'hyper Lordosis', 'پشت صاف': 'Flat Back', 'زانوی عقب رفته': 'Hyperextended Knee', 'زانوی خمیده': 'Flexed Knee', 'کج گردنی یا چرخش گردن': 'Torticollis', 'شانه نابرابر': 'Uneven Shoulders', 'کتف بالدار': 'Winging Scapula', 'انحراف جانبی ستون فقرات': 'Scoliosis', 'انحراف جانبی لگن': 'Uneven Hips', 'چرخش خارجی پا': 'toeing out', 'چرخش داخلی پا': 'Toeing in', 'چرخش مچ پا به داخل': 'Pronation', 'چرخش مچ پا به خارج': 'Supination', 'زانو پرانتزی': 'Genu Varum', 'زانو ضربدری': 'Genu Valgum', 'کف پای صاف': 'Flat Foot', 'کف پای گود': 'High Arch Foot', 'اسکات قدامی صاف شدن پاها': 'OverheadSquat_FeetFlatten', 'اسکات قدامی چرخش به خارج پاها': 'OverheadSquat_FeetTurnOut', 'اسکات قدامی حرکت زانوها به داخل': 'OverheadSquat_KneesMoveInward', 'اسکات قدامی حرکت زانوها به خارج': 'OverheadSquat_KneesMoveOutward', 'اسکات جانبی گود شدن کمر': 'OverheadSquat_LowBackArches', 'اسکات جانبی کمر صاف': 'OverheadSquat_LowBackRounds', 'اسکات جانبی خمیدگی به جلو': 'OverheadSquat_ExcessiveForwardLean', 'اسکات جانبی دست ها در جلو': 'OverheadSquat_ArmsFallForward', 'اسکات خلفی صاف شدن پا': 'OverheadSquat_FeetFlatten', 'اسکات خلفی بلند شدن پاشنه': 'OverheadSquat_HeelsRiseOffFloor', 'اسکات خلفی انتقال نامتقارن ': 'OverheadSquat_AsymmetricWeightShift', 'راه رفتن صاف شدن پاها و چرخش زانو به داخل': 'Gait_FeetFlatten', 'راه رفتن گود شدن کمر': 'Gait_LowBackArches', 'راه رفتن شانه ها گرد می شود': 'Gait_ShouldersRound', 'راه رفتن سر به جلو': 'Gait_HeadForward', 'راه رفتن صاف شدن و چرخش به خارج پاها': 'Gait_FeetTurnOut', 'راه رفتن چرخش بیش از حد لگن': 'Gait_ExcessivePelvicRotation', 'راه رفتن بالا آمدن ران': 'Gait_HipHikes', 'اسکات تک پا حرکت زانو به داخل': 'SingleLegSquat_KneeMovesInward', 'اسکات تک پا بالا آمدن ران': 'SingleLegSquat_HipHikes', 'اسکات تک پا سقوط ران': 'SingleLegSquat_HipDrops', 'اسکات تک پا چرخش داخلی تنه': 'SingleLegSquat_TorsoRotatesInward', 'اسکات تک پا چرخش خارجی تنه': 'SingleLegSquat_TorsoRotatesOutward', 'چرخش دست ها بالاآمدن شانه ها': 'ShoulderRotationTest_ShouldersElevate', 'چرخش دست ها پروترکشن شانه ها': 'ShoulderRotationTest_ShouldersProtract', 'چرخش داخلی دست ها فاصله از دیوار': 'ShoulderRotationTest_HandsFarfromWallInternalRotation', 'چرخش خارجی دست ها فاصله از دیوار ': 'ShoulderRotationTest_HandsFarfromWallExternalRotation', 'دور شدن دست ها بالا آمدن شانه': 'ShoulderAbductionTest_ShouldersElevate', 'دور شدن دست ها پروتکشن شانه': 'ShoulderAbductionTest_ShouldersProtract', 'دور شدن دست ها خم شدن آرنج ها': 'ShoulderAbductionTest_ElbowsFlex', 'خم شدن دست ها بالاآمدن شانه': 'ShoulderFlexionTest_ShouldersElevate', 'خم شدن دست ها گود شدن کمر': 'ShoulderFlexionTest_LowBackArches', 'خم شدن دست ها خم شدن آرنج': 'ShoulderFlexionTest_ElbowsFlex', 'شنا گود شدن کمر': 'PushUp_LowBackSags', 'شنا صاف شدن کمر': 'PushUp_LowBackRounds', 'شنا بالا آمدن شانه': 'PushUp_ShouldersElevate', 'شنا بالی شدن کتف': 'PushUp_ScapulaeWings', 'شنا هایپراکستنشن گردن': 'PushUp_CervicalSpineHyperextends','بدشکلی انگشتان پا':'Deformityofthetoes','بدشکلی انگشتان دست':'DeformityofFingers','سینه فرو رفته':'FunnelChest','سینه کبوتری':'PigeonChest'}
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
    if names==[]:   return []
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
        if item[1]=='5' or n==0:  break
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
            #exer_name = translate[exer[i]].replace('_','\\')
            exer_name = "Genu Varum"
            res.append(random_name_list(int(pro[2*j]),f'{root}\\{exer_name}\\{kind[pro[2*j+1]]}'))
        result.append(res)
    return result



file = pd.read_excel('excel.xlsx',0,dtype='str',keep_default_na= False)

data = {f"{file['gender'][i]} {file['name'][i]} {file['family'][i]}":merge_dict({name:file[name][i] for name in file.columns},{"STATIC":sorted(tuple(file.iloc[i,24:50].items()),key=lambda x:x[1]),"DYNAMIC":sorted(tuple(file.iloc[i,50:88].items()),key=lambda x:x[1],reverse=True)}) for i in range(len(file['name']))}
for key,value in data.items():
    temp = value
    temp['Program']=get_programs(value['STATIC'],value['DYNAMIC'],str(value['PERSON_LEVEL']))
    data[key]=temp



# import pprint
# pprint.PrettyPrinter(indent=4,width=50).pprint(my_print) 
# pprint.PrettyPrinter(indent=4,width=30).pprint(data)    
save_object(data,'data')