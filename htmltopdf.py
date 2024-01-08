import pickle
from bs4 import BeautifulSoup
import re
from PIL import Image
from numpy import imag

main_information_tag = '''
                    <div class="flex flex-col justify-around border-l-2 border-third divide-y divide-third">
                        <span class="row-title">
                            <span>تمرین</span>
                            <!-- these spans should be changed -->
                            <span>exna1</span>
                        </span>
                        <span class="row-title">
                            <span>تکرار</span>
                            <span>12</span>
                        </span>
                        <span class="row-title">
                            <span>ست</span>
                            <span>4</span>
                        </span>
                        <span class="row-title">
                            <span>شدت</span>
                            <span>70-80%</span>
                        </span>
                        <span class="row-title">
                            <span>ضرب آهنگ</span>
                            <span>2 /0/2</span>
                        </span>
                        <span class="row-title">
                            <span>استراحت</span>
                            <span>60-90 ثانیه</span>
                        </span>
                        <span class="row-title">
                            <span>توضیحات</span>
                            <span>سوپر ست</span>
                        </span>
                    </div>
            '''
day = {0:'روز اول' , 1: 'روز دوم' , 2:'روز سوم'  , 3:'روز چهارم'  , 4:"روز پنجم"}
person_level = {'بی تحرک':('Beginner' , 'Beginner') , 'بسیار فعال' : ('Beginner' , 'Intermediate' , 'Advanced' , 'Advanced'), 'نسبتا فعال' : ('Beginner' , 'Intermediate' , 'Intermediate') , 'کم تحرک':('Beginner' , 'Intermediate' , 'Intermediate') , 'بیش از حد فعال':('Intermediate' , 'Intermediate' , 'Advanced' , 'Advanced')}
kind = {0:"Cardio" ,1 : 'Core' , 2: 'Balance', 3: 'Whole body' , 4: 'Strengthing' , 5: 'Stretching'}

#physical_activity = {"مقدار تحرک":(listindex , level)}
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)

def find_range_string(x , from_text):
    pattern = re.compile(x) #the pattern which i want to search for
    result = re.search(x , from_text) 
    return result.span()

def replacing(to_remove : str , to_replace : str , maintext : str):
    range1 = find_range_string(to_remove , maintext)
    intt = range1[0]
    final = range1[1]
    return maintext.replace(maintext[intt:final] , to_replace)

def make_img_tag(address : str):
    str_img_tag = '<img src="./src/images/Exercise.jpg" class="h-[2.2cm]" alt="exercise-pic" />'
    pattern = re.compile(r'src=".+" class=') #the pattern which i want to search for
    result = re.search(pattern , str_img_tag) 
    range1 = result.span() #returns a range of matched substring
    str_img_tag = str_img_tag.replace(str_img_tag[range1[0] + 4 : range1[1]-7] , f'{address}') #replacing last address with a new one!
    return str_img_tag

def return_image_tag(addresslist : list):
    x = '''
    <div class="flex p-2 justify-center items-center gap-1 w-full">
    place_all_image_tags_here!
    </div>
    '''
    images_tag = ''''''
    if len(addresslist) == 0:
        return
    else:
        horizental = None
        img = Image.open('.\\' + addresslist[0])
        width,height = img.size 
        if width > height:
            horizental = True
        else:
            horizental = False
        for i in addresslist:
            if horizental:
                images_tag += f'''
                        <div id="horizental-img">
                            <img src="..\\{i}" alt="exercise-pic">
                        </div>
                        '''
            else:
                images_tag += f'''
                        <div id="vertical-img">
                            <img src="..\\{i}" alt="exercise-pic">
                        </div>
                        '''
        return  f'''
                <div class="flex p-2 justify-center items-center gap-1 w-full">
                {images_tag}
                </div>
                '''

data = load_object('data')
u = 0
for person_data in data:
    main_html_text = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sport Program</title>
        <link rel="stylesheet" href="./src/css/output.css">
    </head>
    <body dir="rtl">
    
        <section class="p-6">
            <!-- Information -->
            <div class="py-1 bg-second text-main">
                <div class="flex justify-center items-center gap-x-8">
                    <div class="space-y-2">
                        <p class="text-center">سن</p>
                        <p class="text-center">age_number1234</p>
                    </div>
                    <div class="space-y-2">
                        <p class="text-center">نام و نام خانوادگی</p>
                        <p class="text-center">persons_name1234</p>
                    </div>
                    <div class="space-y-2">
                        <p class="text-center">BMI</p>
                        <p class="text-center">BMI_of_the_person</p>
                    </div>
                </div>            
            </div>
            junkstring
        </section>
    </body>
    """
    all_tables = ''''''
    main_html_text = replacing('persons_name1234' , str(person_data) , main_html_text)
    main_html_text = replacing('BMI_of_the_person' , str(int(float(data[str(person_data)]['BMI_VALUE']))) , main_html_text)
    main_html_text = replacing('age_number1234' , str(data[person_data]['سن']) , main_html_text)
    exercise_program = data[person_data]['Program']
    day_number = 0
    for each_day in exercise_program:
        table_tag = '''
            <div id="table-container">
                <div id="table-header">
                    123day_number123 
                </div>
                <div id="table-body">
                    tablerooooooooooooows
                </div>
            </div>
    '''
        all_exercises = [x for i in each_day for x in i]
        all_exercises.sort(key=lambda x:len(x[1]) , reverse=True)
        rows_tag = ''''''
        for exercise in all_exercises:
            tag_of_each_row = ''''''
            information_tag = main_information_tag
            information_tag = replacing('exna1' , exercise[0] , information_tag)
            if len(exercise[1]) > 2:
                tag_of_each_row = f'''
                    <div class="tbl-row">
                    {information_tag}
                    {return_image_tag(list(exercise[1]))}
                    </div>
            '''
            elif len(exercise) == 0:
                continue
            else:
                 tag_of_each_row = f'''
                    <div class="tbl-row" id="one-col">
                    {information_tag}
                    {return_image_tag(list(exercise[1]))}
                    </div>
            '''
            rows_tag += tag_of_each_row
        table_tag = replacing('123day_number123' , day[day_number] , table_tag)
        table_tag = replacing('tablerooooooooooooows' , rows_tag , table_tag)
        all_tables += table_tag
        day_number += 1
    main_html_text = replacing('junkstring' , all_tables , main_html_text)
    with open("sport-program-build-new-version\\" + f'newFile{u}.html' , 'w' , encoding='utf-8') as f:
        f.write(main_html_text)
    u += 1

                
