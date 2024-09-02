import datetime
import requests
import pdfplumber
import re

def get_academic_year_and_semester(input_date = datetime.date.today()):    
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
    academic_year, semester = get_academic_year_and_semester(input_date)
    current_year = input_date.year
    pdf_content = fetch_pdf_content(academic_year)
    if semester == 1:
        pattern = r"九\n月([\s\S]+?)十\n月"
        start_month = 9
        match = re.search(pattern, pdf_content)
        if match:
            print(match.group(0))
    else:
        pattern = r"二\n月([\s\S]+?)三\n月"
        start_month = 2
        match = re.search(pattern, pdf_content)
        if match:
            print(match.group(0))
    start_date = None
    for line in match.group(0).split('\n'):
        if '開學日' in line:
            print(line)
            if line[0].isdigit():
                start_date = datetime.date(current_year, start_month, int(line.split("日")[0]))
            elif line.split("日")[0][-1].isdigit():
                start_date = datetime.date(current_year, start_month, int(line.split("日")[0].split(" ")[-1]))
            else:
                raise ValueError("找不到開學日")
            break
    return academic_year, semester, start_date

print(semester_start_date(datetime.date(2022, 10, 1)))