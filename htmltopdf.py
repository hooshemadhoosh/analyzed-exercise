import pickle
import re
from PIL import Image
from numpy import imag

pure_html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sport Program</title>
        <link rel="stylesheet" href="./src/css/output.css">
    </head>
    <body dir="rtl">
        <section class="p-2">
            <!-- Information -->
            <div class="information">
                <div class="flex justify-center items-center gap-x-8">
                    <div class="space-y-2">
                        <p class="text-center">سن</p>
                        <p class="text-center">PUT_AGE_HERE!</p>
                    </div>
                    <div class="space-y-2">
                        <p class="text-center">نام و نام خانوادگی</p>
                        <p class="text-center">PUT_PERSON_NAME_HERE!</p>
                    </div>
                    <div class="space-y-2">
                        <p class="text-center">BMI</p>
                        <p class="text-center">PUT_BMI_VALUE_HERE!</p>
                    </div>
                </div>            
            </div>
            PUT ALL TABLES HERE!
        </section>
    </body>
    </html>
"""

information_in_row = '''
                    <div class="texts-container">
                        <span class="row-title">
                            <!-- these spans should be changed -->
                            <span>تمرین</span>
                            <span>exna1</span>
                        </span>
                        <div class="flex divide-x divide-x-reverse divide-third">                       
                            <span class="row-title w-10 flex-shrink-0">
                                <span>تکرار</span>
                                <span>12</span>
                            </span>
                            <span class="row-title">
                                <span>شدت</span>
                                <span>70-80%</span>
                            </span>
                        </div>
                        <div class="flex divide-x divide-x-reverse divide-third">
                            <span class="row-title w-10 flex-shrink-0">
                                <span>ست</span>
                                <span>4</span>
                            </span>
                            <span class="row-title">
                                <span>ضرب آهنگ</span>
                                <span>2 /0/2</span>
                            </span>
                        </div>
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
#physical_activity = {"مقدار تحرک":(listindex , level)}
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)

def find_range_string(x , from_text):
    result = re.search(x , from_text) 
    return result.span()

def replacing(to_remove : str , to_replace : str , maintext : str):
    range1 = find_range_string(to_remove , maintext)
    intt = range1[0]
    final = range1[1]
    return maintext.replace(maintext[intt:final] , to_replace)


def return_image_tag(addresslist : list):
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
                <div class="images-container">
                {images_tag}
                </div>
                '''

data = load_object('data')
for person_data in data:
    main_html_text = pure_html_code
    all_tables = ''''''
    main_html_text = replacing('PUT_PERSON_NAME_HERE!' , str(person_data) , main_html_text)
    main_html_text = replacing('PUT_BMI_VALUE_HERE!' , str(int(float(data[str(person_data)]['BMI_VALUE']))) , main_html_text)
    main_html_text = replacing('PUT_AGE_HERE!' , str(data[person_data]['سن']) , main_html_text)
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
            information_tag = information_in_row
            information_tag = replacing('exna1' , exercise[0] , information_tag)
            if len(exercise[1]) > 2:
                tag_of_each_row = f'''
                    <div class="tbl-row">
                    {information_tag}
                    {return_image_tag(list(exercise[1]))}
                    </div>
            '''
            elif len(exercise[1]) == 0:
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
    main_html_text = replacing('PUT ALL TABLES HERE!' , all_tables , main_html_text)
    if data[person_data]['gender'] != 'میانگین':
        file_name = str(person_data).replace(' ' , '_' )
        with open("sport-program-build\\" + f'{file_name}.html' , 'w' , encoding='utf-8') as f:
            f.write(main_html_text)


                
