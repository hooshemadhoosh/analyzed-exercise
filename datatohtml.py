import pickle
from pydoc import html
import re
from PIL import Image

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
        :root {
        --main-color: #put_main_color_here;
        --second-color: #put_second_color_here;
        --third-color: #put_third_color_here;
        --font-base: 14px;
        --font-sm: 12px;
        --font-xs: 10px;
        --font-2xs: 8px;
        --font-3xs: 6px;
    }
    * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    }
    @page {
        margin: 0;
        padding: 0;
        size: 8.3in 11.7in;
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
        background-color: var(--second-color);
        color: var(--main-color);
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
        border: 2px solid var(--third-color);
        background-color: var(--third-color);
        color: var(--second-color);
        text-align: center;
        font-size: 12px;
        font-weight: bold;
    }

    #table-body {
        width: 100%;
        display: flex;
        flex-wrap: wrap;
        gap: 4px;
    }

    .tbl-row {
        width: 100%;
        display: grid;
        grid-template-columns: 120px 1fr;
        grid-template-rows: 150px;
        background-color: var(--main-color);
        color: var(--second-color);
    }

    #one-col {
        width: calc(50% - 2px);
    }

    .texts-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        border-left: 2px solid var(--third-color);
    }

    .texts-container > * {
        border-top: 1px solid var(--third-color);
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
        border-left: 1px solid var(--third-color);
    }

    .row-title span:first-child {
        font-size: 6px;
        padding-left: 2px;
        border-left: 1px solid var(--third-color);
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

    .empty-div {
        width: 100%;
        background-color: #ffffff;
    }

    #table-container-text {
        margin-bottom: 20px;
    }
    table {
        width: 100%;
        text-align: center;
        border-collapse: collapse;
        color: var(--second-color);
        margin-top: 15px;
    }
    table:first-child {
        margin-top: 0;
    }
    thead {
        background-color: var(--third-color);
    }
    tbody {
        margin-top: 10px;
        background-color: var(--main-color);
    }
    th {
        padding: 4px;
        font-size: var(--font-sm);
        border: 1px solid var(--main-color);
    }
    td {
        padding: 2px;
        font-size: 9px;
        border: 1px solid var(--third-color);
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

txt_table_container = '''
        <div id="table-container-text">
            
            <table>
                <thead>
                    <tr>
                        <th colspan="7">number_of_day</th>
                    </tr>
                    <tr>
                        <th>تمرین</th>
                        <th>تکرار</th>
                        <th>ست</th>
                        <th>شدت</th>
                        <th>ضرب آهنگ</th>
                        <th>استراحت</th>
                        <th>توضیحات</th>
                    </tr>
                </thead>

                <tbody>
                    PUT_ALL_TXT_ROWS_HERE
                </tbody>
            </table>
        </div>
'''

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
    
def check_height(ocupied_height : int , last_html_tag : str , height_last_tag_to_add : int):
    standard_page_height = 1122 - (2*8)
    if ocupied_height > standard_page_height:
        difference = standard_page_height - ocupied_height + height_last_tag_to_add + 20
        ocupied_height = height_last_tag_to_add
        empty_tag = f'''<div class="empty-div" style="height: {int(difference)}px">
                        </div>'''
        last_html_tag = empty_tag + last_html_tag
    return ocupied_height , last_html_tag

def chang_color(htmltext , gender):
    if gender == 'سرکار خانم':
        #main_color = 'ff0a54' #pink color
        #sec_color = 'fae0e4' #Black color
        #third_color = 'ff99ac' #gray color
        main_color = 'ffffff'
        sec_color = '000000'
        third_color = '505052'
    else:
        #main_color = '03045e'
        #sec_color = 'ffffff'
        #third_color = '0077b6'
        main_color = 'ffffff'
        sec_color = '000000'
        third_color = '505052'
    htmltext = replacing('put_main_color_here' , main_color , htmltext)
    htmltext = replacing('put_second_color_here' , sec_color , htmltext)
    htmltext = replacing('put_third_color_here' , third_color , htmltext)
    return htmltext

data = load_object('data')
for person_data in data:
    main_html_text = pure_html_code
    all_tables = ''''''
    all_txt_table_tags = ''''''
    main_html_text = replacing('PUT_PERSON_NAME_HERE!' , str(person_data) , main_html_text)
    main_html_text = replacing('PUT_BMI_VALUE_HERE!' , str(int(float(data[str(person_data)]['BMI_VALUE']))) , main_html_text)
    main_html_text = replacing('PUT_AGE_HERE!' , str(data[person_data]['سن']) , main_html_text)
    main_html_text = chang_color(main_html_text , data[person_data]['gender'])
    exercise_program = data[person_data]['Program']
    day_number = 0
    for each_day in exercise_program:
        text_table_tag = txt_table_container
        img_table_tag = '''
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
        rows_tag = ''''''
        all_txt_row_tag = ''''''
        for exercise in all_exercises:
            txt_row_tag = '''
                    <tr>
                        <td>exercise_name</td>
                        <td>12</td>
                        <td>4</td>
                        <td>70-80%</td>
                        <td>2/0/2</td>
                        <td>60-90 ثانیه</td>
                        <td>سوپرست</td>
                    </tr>
                '''
            this_row_tag = ''''''
            information_tag = information_in_row
            txt_row_tag = replacing('exercise_name' , exercise[0] , txt_row_tag)
            information_tag = replacing('exna1' , exercise[0] , information_tag)
            this_row_tag += f'''
                <div class="tbl-row">
                {information_tag}
                {return_image_tag(list(exercise[1]))}
                </div>
            '''
            rows_tag += this_row_tag
            all_txt_row_tag += txt_row_tag
        img_table_tag = replacing('123day_number123' , day[day_number] , img_table_tag)
        text_table_tag = replacing('number_of_day' , day[day_number] , text_table_tag)
        img_table_tag = replacing('tablerooooooooooooows' , rows_tag , img_table_tag)
        text_table_tag = replacing('PUT_ALL_TXT_ROWS_HERE' , all_txt_row_tag , text_table_tag)
        all_tables += img_table_tag
        all_txt_table_tags += text_table_tag
        day_number += 1
    all_tables = all_txt_table_tags + all_tables
    main_html_text = replacing('PUT ALL TABLES HERE!' , all_tables , main_html_text)
    if data[person_data]['gender'] != 'میانگین':
        file_name = str(person_data).replace(' ' , '_' )
        with open("sport-program-build\\" + f'{file_name}.html' , 'w' , encoding='utf-8') as f:
            f.write(main_html_text)


                
