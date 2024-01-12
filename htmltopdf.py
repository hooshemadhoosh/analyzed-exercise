import pickle
import re
from PIL import Image
import os

pure_html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sport Program</title>
        <!--<link rel="stylesheet" href="file:///C:/Users/Padidar/analyzed-exercise/sport-program-build/src/css/main.css">-->
    </head>
    <style>
    * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    }

    @font-face {
        font-family: "Vazir";
        src: url("./src/fonts/Vazir-FD-WOL.ttf");
    }

    body {
        font-family: "Vazir";
        font-size: 14px;
        overflow-x: hidden;
        margin: auto;
        width: 210mm;
    }

    section {
        padding: 8px;
    }

    img {
        max-width: 100%;
    }

    .information {
        display: inline-block;
        position: relative;
        right: 50%;
        transform: translateX(50%);
        padding: 4px 24px;
        background-color: #e8e8e8;
        color: #101830;
        font-size: 10px;
    }

    .information_contianer {
        display: flex;
        justify-content: center;
        align-items: center;
        column-gap: 32px;
    }

    .information_texts {
        text-align: center;
    }
    .information_texts *:first-child {
        margin-bottom: 6px;
    }

    #table-header {
        padding: 4px 0;
        border: 2px solid #505052;
        background-color: #505052;
        color: #e8e8e8;
        text-align: center;
        font-size: 12px;
        font-weight: bold;
    }

    #table-body {
        width: 100%;
        display: flex;
        flex-wrap: wrap;
        gap: 4px;
        margin-bottom: 10%;
    }

    .tbl-row {
        width: 100%;
        display: grid;
        grid-template-columns: 120px 1fr;
        grid-template-rows: 150px;
        background-color: #101830;
        color: #e8e8e8;
    }

    #one-col {
        width: calc(50% - 2px);
    }

    .texts-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        border-left: 2px solid #505052;
    }

    .texts-container > * {
        border-top: 1px solid #505052;
    }
    .texts-container > *:first-child {
        border-top: 0;
    }

    .row-title {
        display: flex;
        align-items: center;
        padding: 4px;
    }

    .row-title_two-col {
        display: flex;
    }
    .row-title_two-col > *:first-child {
        width: 40px;
        flex-shrink: 0;
        border-left: 1px solid #505052;
    }

    .row-title span:first-child {
        font-size: 6px;
        padding-left: 2px;
        border-left: 1px solid #505052;
    }
    .row-title span:last-child {
        font-size: 9px;
        padding-right: 4px;
    }

    .texts-container > .row-title:first-child,
    .texts-container > .row-title:last-child {
        flex-grow: 1;
    }

    .images-container {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        column-gap: 2px;
        padding: 4px;
    }

    #vertical-img {
        height: 95%;
    }
    #vertical-img img {
        height: 100%;
    }

    #horizental-img {
        width: 128px;
    }
    </style>
    <body dir="rtl">
        <section class="p-2">
            <div class="information">
                <div class="information_contianer">
                    <div class="information_texts">
                        <p>سن</p>
                        <p>PUT_AGE_HERE!</p>
                    </div>
                    <div class="information_texts">
                        <p>نام و نام خانوادگی</p>
                        <p>PUT_PERSON_NAME_HERE!</p>
                    </div>
                    <div class="information_texts">
                        <p>BMI</p>
                        <p>PUT_BMI_VALUE_HERE!</p>
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
                            <span>تمرین</span>
                            <span>exna1</span>
                        </span>
                        <div class="row-title_two-col">                       
                            <span class="row-title">
                                <span>تکرار</span>
                                <span>12</span>
                            </span>
                            <span class="row-title">
                                <span>شدت</span>
                                <span>70-80%</span>
                            </span>
                        </div>
                        <div class="row-title_two-col">
                            <span class="row-title">
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
nnnnn= 0
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
        nnnnn += 1
        file_name = str(person_data).replace(' ' , '_' )
        with open("sport-program-build\\" + f'file{nnnnn}.html' , 'w' , encoding='utf-8') as f:
            f.write(main_html_text)


                
