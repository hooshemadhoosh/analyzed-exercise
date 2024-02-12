import pickle
from pydoc import html
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
    thead {
        display: table-row-group;
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
        font-size: 7px;
        padding-right: 1px;
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
        height=56
        <div id="table-container-text">
            <table>
                <thead>
                    <tr>
                        <th colspan="7">حرکات اصلاحی</th>
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
                                <span>repeatations</span>
                            </span>
                            <span class="row-title">
                                <span>شدت</span>
                                <span>70-80%</span>
                            </span>
                        </div>
                        <div class="row-title_two-col">
                            <span class="row-title">
                                <span>ست</span>
                                <span>the_number_of_the_sets</span>
                            </span>
                            <span class="row-title">
                                <span>ضرب آهنگ</span>
                                <span>zarb_ahang</span>
                            </span>
                        </div>
                        <span class="row-title">
                            <span>استراحت</span>
                            <span>rest_time</span>
                        </span>
                        <span class="row-title">
                            <span>توضیحات</span>
                            <span>سوپر ست</span>
                        </span>
                    </div>
            '''

container_of_img_table_tags = '''
            <div id="table-container">
                height=30
                <div id="table-header">
                    حرکات اصلاحی 
                </div>
                <div id="table-body">
                    Put_all_img_table_rows_here!
                </div>
            </div>
            '''

source_txt_row_tag = '''
                    height=19
                    <tr>
                        <td>exercise_name</td>
                        <td>repeatations</td>
                        <td>the_number_of_the_sets</td>
                        <td>70-80%</td>
                        <td>zarb_ahang</td>
                        <td>rest_time</td>
                        <td>سوپرست</td>
                    </tr>
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
        main_color = 'ff0a54' #pink color
        sec_color = 'fae0e4' #Black color
        third_color = 'ff99ac' #gray color
        main_color = 'ffffff'
        sec_color = '000000'
        third_color = '505052'
    else:
        main_color = '03045e'
        sec_color = 'ffffff'
        third_color = '0077b6'
        main_color = 'ffffff'
        sec_color = '000000'
        third_color = '505052'
    htmltext = replacing('put_main_color_here' , main_color , htmltext)
    htmltext = replacing('put_second_color_here' , sec_color , htmltext)
    htmltext = replacing('put_third_color_here' , third_color , htmltext)
    return htmltext

def height_checker(final_html_str : str):
    ocupied_h = 54
    standard_height = 1123 - (2*8)
    while True:
        result = re.search(r'height=\d+' , final_html_str)
        if result == None:
            break
        start = result.span()[0]
        end = result.span()[1]
        numRange = re.search(r'\d+' , final_html_str[start:end]).span()
        numstart = numRange[0]
        numend = numRange[1]
        last_elemant_h = int(final_html_str[start:end][numstart:numend])
        ocupied_h += last_elemant_h
        if ocupied_h >= standard_height:
            difference = standard_height - (ocupied_h - last_elemant_h)
            final_html_str = final_html_str.replace(final_html_str[start:end] , f'''<div class="empty-div" style="height: {int(difference)}px">
            </div>''' , 1)
            ocupied_h = last_elemant_h 
        else:
            final_html_str = final_html_str.replace(final_html_str[start:end] , '' , 1)
    return final_html_str

phases = load_object('./Phase/Phase 1')
data = load_object('data')
for person_data in data:
    main_html_text = pure_html_code
    main_html_text = replacing('PUT_PERSON_NAME_HERE!' , str(person_data) , main_html_text)
    main_html_text = replacing('PUT_BMI_VALUE_HERE!' , str(int(float(data[str(person_data)]['BMI_VALUE']))) , main_html_text)
    main_html_text = replacing('PUT_AGE_HERE!' , str(data[person_data]['سن']) , main_html_text)
    main_html_text = chang_color(main_html_text , data[person_data]['gender'])
    exercise_program = data[person_data]['Program']
    text_table_tag = txt_table_container
    img_table_tag = container_of_img_table_tags
    rows_tag = ''''''
    all_txt_row_tag = ''''''
    for ttype in exercise_program:
        for exercise in ttype:
            txt_row_tag = source_txt_row_tag
            information_tag = information_in_row
            this_row_tag = ''''''
            txt_row_tag = replacing('exercise_name' , exercise[1][0] , txt_row_tag)
            information_tag = replacing('exna1' , exercise[1][0] , information_tag)
            # THESE ARE TAGS TO ADD INFORMATION OF PHASES IN HTML TAGS
            # type_exe = exercise[1][0].split('\\')[1]
            # dict_this_type = phases[type_exe]
            # information_tag , txt_row_tag = replacing('repeatations' , str(dict_this_type['تکرار']) , information_tag) , replacing('repeatations' , str(dict_this_type['تکرار']) , txt_row_tag)
            # information_tag , txt_row_tag = replacing('the_number_of_the_sets' , str(dict_this_type['ست']) , information_tag) , replacing('the_number_of_the_sets' , str(dict_this_type['ست']) , txt_row_tag)
            # information_tag , txt_row_tag = replacing('rest_time' , str(dict_this_type['استراحت']) , information_tag) , replacing('rest_time' , str(dict_this_type['استراحت']) , txt_row_tag)
            # information_tag , txt_row_tag = replacing('zarb_ahang' , str(dict_this_type['ضرب آهنگ']) , information_tag) , replacing('zarb_ahang' , str(dict_this_type['ضرب آهنگ']) , txt_row_tag) 
            addresses = [os.path.join('.\\' , exercise[0] , i) for i in exercise[1][1]]
            this_row_tag += f'''
                height=150
                <div class="tbl-row">
                {information_tag}
                {return_image_tag(addresses)}
                </div>
            '''
            rows_tag += this_row_tag
            all_txt_row_tag += txt_row_tag
    img_table_tag = replacing('Put_all_img_table_rows_here!' , rows_tag , img_table_tag)
    text_table_tag = replacing('PUT_ALL_TXT_ROWS_HERE' , all_txt_row_tag , text_table_tag)
    all_tables = text_table_tag + img_table_tag
    main_html_text = replacing('PUT ALL TABLES HERE!' , all_tables , main_html_text)
    if data[person_data]['gender'] != 'میانگین':
        main_html_text = height_checker(main_html_text)
        file_name = str(person_data).replace(' ' , '_' )
        with open("sport-program-build\\" + f'{file_name}.html' , 'w' , encoding='utf-8') as f:
            f.write(main_html_text)


                
