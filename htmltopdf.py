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

#import pprint 
#pprint.PrettyPrinter(indent=4,width=30).pprint(data)    
#data = {'40230853' : {'BMI' : 'Thin' , 'Program' : [[[('excercise nameA1' , ['first adress' , 'second address']) , ('excersise nameA2' , []) , (...)] , [('excerciseB1' , ['address1' , 'address2'])]] , [] , []] }}

# u = 0

# #ATTENTION! THE student number isn't string! it is an unknown type! 
# for person in data:
#     u += 1
#     htmlfile = open('sport-program-build\index.html' , 'r' , encoding='utf8')
#     index = htmlfile.read()
#     soup = BeautifulSoup(index , 'html.parser')

#     #------general information------------
#     age = int(float(data[str(person)]['سن']))
#     bmi = str(int(float(data[person]['BMI_VALUE'])))

#     #finding the paragraph tag which contains the name of the person
#     nameee = soup.find('p' , {'id' : 'name-content'})

#     #changing the p tag where it contains some letters and replace it with the string form of the person!
#     new_text = nameee.find(text=re.compile(r'^[\u0600-\u06FF\s]+$')).replace_with(str(person))
#     #'^[\u0600-\u06FF\s]+$' THIS IS A REGEX FOR ALL PERSIAN/ARRABIC LETTERS!

#     agechanging = soup.find('p' , {'id':'age-content'}).find(text=re.compile(r'\d+')).replace_with(str(age))

#     bmichange =  soup.find('p' , {'id':'BMI-content'}).find(text=re.compile(r'\d+')).replace_with(bmi)

#     try:
#         each_day_level = person_level[data[str(person)]['PERSON_LEVEL']]
#     except KeyError:
#         each_day_level = 'نسبتا فعال'

#     exc_program = data[str(person)]['Program']
#     print (exc_program)
#     for i in range(len(exc_program)):
#         level = each_day_level[i]
#         #merging all type of exercises in one list which contains some tuples 
#         #whose first element is the name of exercise and the second one is a tuple of image addresses
#         exercises = [e for k in exc_program for e1 in k for e in e1] 
#         day_num = day[i]
#         #making table tage
#         table = BeautifulSoup('<div id="table-body"></div>' , 'html.parser')
#         table_header_string =   '''
#                 <!-- Table Header -->
#                 <div id="table-header">
#                     <h2 class="py-2 text-center font-bold text-lg">
#                         روز اول
#                     </h2>
#                     <div class="flex text-center font-bold border-t-2 border-orange-200">
#                         <span class="py-1 w-[218px] row-title">تمرین</span>
#                         <span class="py-1 w-[60px] row-title">تکرار</span>
#                         <span class="py-1 w-[60px] row-title">ست</span>
#                         <span class="py-1 w-[100px] row-title">شدت</span>
#                         <span class="py-1 w-[120px] row-title">ضرب آهنگ</span>
#                         <span class="py-1 w-[120px] row-title">استراحت</span>
#                         <span class="py-1 w-[120px] row-title">توضیحات</span>
#                     </div>
#                 </div>
#                                 '''
#         table_header = BeautifulSoup(table_header_string , 'html.parser')
#         commit_day_number = table_header.find('h2' , {'class' : 'py-2 text-center font-bold text-lg'}).find(text=re.compile(r'.+')).replace_with(day_num)
#         #rownum = 0
#         for exercise in exercises:
#             #rownum += 1
#             #making the tag of a row of table
#             row_html_str ="""
#             <!-- Each Row -->
#                     <div class="tbl-row">
#                         <div class="flex text-center">
#                             <span class="py-2 w-[218px] row-title" id="exercise-name">اسکوات با تی آر ایکس</span>
#                             <span class="py-2 w-[60px] row-title" id="repeation">12</span>
#                             <span class="py-2 w-[60px] row-title" id="set">4</span>
#                             <span class="py-2 w-[100px] row-title" id="intensity">70-80%</span>
#                             <span class="py-2 w-[120px] row-title" id="beat">2 /0/2</span>
#                             <span class="py-2 w-[120px] row-title" id="relaxation-time">60-90 ثانیه</span>
#                             <span class="py-2 w-[120px] row-title" id="explanation">سوپر ست</span>
#                         </div>
#                         <div class="flex justify-around" id="image-container">
                            
#                         </div>
#                     </div>
#                     """
#             row = BeautifulSoup(row_html_str , 'html.parser')

#             #change the exercise name with a new one
#             tempor = row.find('span' , {'id':'exercise-name'}).find(text=re.compile(r'.+')).replace_with(str(exercise[0]))

#             #finding the kind of the exercise
#             for lev in range(len(exc_program)):
#                 for kindd in range(len(exc_program[lev])):
#                     if exercise in exc_program[lev][kindd]:
#                         kind_of_exercise = kind[kindd]
#                         break


#             all_str_img_tags = ''
#             if len(exercise[1]) > 0:
#                 for i in exercise[1]:
#                     str_img_tag = make_img_tag(f'../{kind_of_exercise}/{level}/' + str(i))
#                     all_str_img_tags += str_img_tag
#             else:
#                 all_str_img_tags = make_img_tag('./src/images/Exercise.jpg')

#             #we have all image tags here!
#             img_tag = BeautifulSoup(all_str_img_tags , 'html.parser')

#             commit_img_tag = row.find('div' , {'id' : 'image-container'}).append(img_tag)
#             #commit_row_num = row.find('span' , {'id':'row-number'}).find(text=re.compile(r'\d+')).replace_with(str(rownum))
#             commit_exer_name = row.find('span' , {'id':"exercise-name"}).find(text=re.compile(r'.+')).replace_with(str(exercise[0]))

#             table.div.append(row)

#         soup.body.section.div.find('div', {'id':'table-container'}).append(table_header)
#         soup.body.section.div.find('div', {'id':'table-container'}).append(table)
#         #print(f'---------------THIS IS THE {i}th table-----------------\n' ,table.prettify())
#                                 #i use \\ instead of \ beacause if it doesn't it made error
#     with open("sport-program-build\\" + f'newFile{u}.html' , 'wb') as f:
#         f.write(soup.prettify("utf-8"))




#html_string = html_string.find_all('img' , src=re.compile(r".+"))
#print (type(html_string[0]))
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

                
