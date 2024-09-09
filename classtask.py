# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:35:52 2024

@author: Tristan
"""

import datetime
import holidays
import requests
import pdfplumber
import re

def strip_by_chinese_comma(astring):
    """
        藉由把中文頓號與英文頓號代換成空白，讓字串可以被正確分割
    """
    if astring == None:
        return astring
    else:
        split_out1=astring.replace('、',' ').replace(',',' ').split()
        return split_out1


def task(asheet):
    amain=[]
    for row in range(3,asheet.max_row):
        single_class=[]
        #date
        class_date= asheet.cell(row,2).value
        if class_date == None:
            single_class.append(class_date)
        else:
            split_out1=class_date.split('(',2)
            for j1 in split_out1:
                single_class.append(j1.strip())
        
        #time
        class_time=asheet.cell(row,3).value
        if class_time ==None:
            single_class.append(class_time)
        else:
            split_out2=class_time.split('M',2)
            for j2 in split_out2:
                single_class.append(j2.strip())        
        single_class.append(strip_by_chinese_comma(asheet.cell(row,5).value))
        #print(single_class)
        amain.append(single_class)

        
    #for four hour class
    for ak in amain:
        if '1-5' in ak:
            ak.append('1-3')
            ak.append('3-5')

    for am in amain:
        if len(am)==7:
            am1=[am[0],am[1],am[2],am[5],am[4]]
            am2=[am[0],am[1],am[2],am[6],am[4]]
            amain.append(am1)
            amain.append(am2)
            amain.remove(am)
    
    return amain


def teachers (class_list):
    final_output=[]
    for every_class in class_list:
        if len(every_class)==5 and every_class[4]!=None:
            
            for teacher in every_class[4]:
                final_output.append([every_class[0],every_class[1],every_class[2],every_class[3],teacher])
        elif every_class[0]==None:
            pass
        
        #有些長度為7的實驗課沒有清乾淨，所以這裡再篩一遍
        elif len(every_class)==7:
            for teacher in every_class[4]:
                final_output.append([every_class[0],every_class[1],every_class[2],every_class[5],teacher])
                final_output.append([every_class[0],every_class[1],every_class[2],every_class[6],teacher])
        else:
            final_output.append(every_class)
            

        
    return final_output

def ChineseYiDate():
    
    all_date=[]
    sorted_date=[]
    days= datetime.date(2024,9,9)
    last_day= datetime.date(2025,1,6)
    while last_day - days >=datetime.timedelta(days=0):
        all_date.append(days)
        days=days + datetime.timedelta(weeks=1)
        
    for raw_date in all_date:
        part_date=raw_date.isoformat().split('-',3)
        part_year=part_date[0]
        part_year=str(int(part_year)-1911)
        sorted_date.append(f'{part_year}/{part_date[1]}/{part_date[2]}')
        
    return sorted_date

def denDate():
    import datetime
    all_date=[]
    sorted_date=[]
    days= datetime.date(2024,9,9)
    last_day= datetime.date(2025,1,6)
    while last_day - days >=datetime.timedelta(days=0):
        all_date.append(days)
        days=days + datetime.timedelta(weeks=1)
        
    for raw_date in all_date:
        part_date=raw_date.isoformat().split('-',3)
        part_year=part_date[0]
        part_year=str(int(part_year)-1911)
        sorted_date.append(f'{part_year}/{part_date[1]}/{part_date[2]}')
        
    return sorted_date

def generate_course_dates_with_holidays(start_date: datetime.date, weekday: int, year: int) -> list:
    """
    生成十八周的課程日期列表，並注記與台灣國定假日重疊的日期。

    :param start_date: 開學日期，格式為 datetime.date。
    :param weekday: 上課的星期幾 (0 = 週一, 1 = 週二, ..., 6 = 週日)。
    :param year: 課程年份，用來查詢國定假日。
    :return: 包含十八個課程日期的列表，每個元素為 (datetime.date, 假日名稱) 或 (datetime.date, None)。
    """
    course_dates = []
    #print(year)
    taiwan_holidays = holidays.TW(years=year,language='zh_TW')+holidays.TW(years=year+1)
    
    # 計算第一周的第一個上課日
    first_class_date = start_date + datetime.timedelta(days=(weekday - start_date.weekday() + 7) % 7)
    
    # 生成十八周的課程日期, 並查詢是否為國定假日
    for week in range(18):
        course_date = first_class_date + datetime.timedelta(weeks=week)
        holiday_name = taiwan_holidays.get(course_date)
        course_dates.append((course_date, holiday_name))
    
    
    return course_dates

def get_academic_year_and_semester(input_date = datetime.date.today()):    
    """
        計算現在或是特定日期是哪一個學年度與哪一個學期。
    """
    year = input_date.year
    month = input_date.month
    
    # 計算學年度
    if month >= 8:
        academic_year = year - 1911
        semester = 1
    else:
        academic_year = year - 1911 - 1
        semester = 2
    
    return academic_year, semester

def fetch_pdf_content(academic_year):
    """
        下載指定學年度的中國醫藥大學校務行事曆 PDF 檔案，並讀取其內容。
    """
    # 替換網址中的學年度部分
    url = f"https://president.cmu.edu.tw/doc/schedule/{academic_year}Schedule.pdf"
    
    # 發送 HTTP 請求來下載 PDF
    response = requests.get(url)
    
    # 確認請求成功
    if response.status_code == 200:
        # 打開 PDF 並讀取內容
        with open('schedule.pdf', 'wb') as file:
            file.write(response.content)
        
        # 使用 pdfplumber 讀取 PDF 文件內容
        with pdfplumber.open('schedule.pdf') as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
        
        return text
    else:
        return f"Failed to retrieve the PDF. Status code: {response.status_code}"
# 使用範例
  
def semester_start_date(input_date = datetime.date.today()):
    """
        取得指定日期的學年度、學期，並找出開學日。
    """
    academic_year, semester = get_academic_year_and_semester(input_date)
    current_year = input_date.year
    pdf_content = fetch_pdf_content(academic_year)
    if semester == 1:
        pattern = r"九\n月([\s\S]+?)十\n月"
        start_month = 9
        match = re.search(pattern, pdf_content)
        if match:
            pass
    else:
        pattern = r"二\n月([\s\S]+?)三\n月"
        start_month = 2
        match = re.search(pattern, pdf_content)
        if match:
            pass
    start_date = None
    for line in match.group(0).split('\n'):
        if '開學日' in line:
            #print(line)
            if line[0].isdigit():
                start_date = datetime.date(current_year, start_month, int(line.split("日")[0]))
            elif line.split("日")[0][-1].isdigit():
                start_date = datetime.date(current_year, start_month, int(line.split("日")[0].split(" ")[-1]))
            else:
                raise ValueError("找不到開學日")
            break
    return academic_year, semester, start_date