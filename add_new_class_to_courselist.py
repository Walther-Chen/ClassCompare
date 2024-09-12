# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:06:34 2024

@author: Tristan
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
from sys import exit
import os
import json

def find_class_name(classes,class_time):
    for count,i in enumerate(classes):
        if i.get_text():
            class_time.append((count,i.get_text()))
            del classes [:7]
            break
    if len(classes)>=7:
        find_class_name(classes,class_time)
    return class_time

def crawl_class_information(dep,cname):
    #設定
    chrome_opt=Options()
    chrome_opt.add_argument('--headless')
    driver= webdriver.Chrome(options=chrome_opt) 
    driver.get('https://web1.cmu.edu.tw/courseinfo/')
    #輸入課程名稱
    element=driver.find_element(By.ID,'Cos_name_q') 
    element.send_keys(cname)
    #按enter
    btn=driver.find_element(By.ID,'JS-search')
    btn.send_keys(Keys.ENTER)
    sleep(5)
    dat=driver.page_source
    driver.close()


    #selenium找不到上課時間的tag，所以用bs爬
    soup=BeautifulSoup(dat,'html.parser')
    #課程名稱
    class_name=[]
    d=soup.find_all('td',{'data-label':"課程名稱"})
    for j in d:
        if j.get_text():
            class_name.append(j.get_text())
    #課程時間
    class_time=[]
    c=soup.find_all('td',class_='ClassTable') #課程時間在classtable這個tag裡
    class_time=find_class_name(c,class_time)
    #系所名稱
    dep_name=[]
    e=soup.find_all('td',{'data-label':"系所年級"})
    for m in e:
        if m.get_text():
            dep_name.append(m.get_text())

    #確認真的是想要的課 
    output=[]    
    for k,name in enumerate(class_name):
        if name == cname:
            if k < len(class_name)/2: #串列後半段是重複的資訊，跟原始碼有關
                if dep_name[k] == dep:
                    if '單' in class_time[k][1]: #處理單雙週問題
                        class_time[k]=(class_time[k][0],class_time[k][1][2:-1])
                        output.append([dep_name[k],name+'(單週)',class_time[k]])
                    elif '雙' in class_time[k][1]:
                        class_time[k]=(class_time[k][0],class_time[k][1][2:-1])
                        output.append([dep_name[k],name+'(雙週)',class_time[k]])
                    else:
                        output.append([dep_name[k],name,class_time[k]])
    
    return output

def postprocess(sclass):
    clean_list=[]
    timedict={'1':(8,9),'2':(9,10),'3':(10,11),'4':(11,12),'5':(13,14),'6':(14,15),'7':(15,16),
              '8':(16,17),'9':(17,18),'A':(18,19),'B':(19,20)}
    exacttime=(timedict[sclass[2][1][0]][0],timedict[sclass[2][1][-1]][1])
    clean_list.append([sclass[0]+sclass[1],sclass[2][0],exacttime])
    
    return clean_list

def number_wrong_interface(res):
    for order,c in enumerate(res):
        print(order+1,'. ','年級：',c[0],'，課程：',c[1],'，星期',c[2][0],'，第',c[2][1][0],'節至第',c[2][1][-1],'節')
    targetclass=input('請輸入欲排課之課程號碼')
    if int(targetclass)>len(res):
        print('invalid choice, please try again.')
        target = number_wrong_interface(res)
        return target
    else:
        target=postprocess(res[int(targetclass)-1])
        return target
    
def write_into_json(aclass):
    #處理字典
    dic_class={'classname': f'{aclass[0][0]}', 'weekday': int(aclass[0][1]), 
               'starttime': int(aclass[0][2][0]), 'endtime': int(aclass[0][2][1])}
    os.chdir(os.path.dirname(__file__))
    with open ('courselist.json','r',encoding='utf-8')as f:
        d=json.load(f)
        if dic_class not in d:
            d.append(dic_class)
    with open ('courselist.json','w+',encoding='utf-8')as f:
        json.dump(d,f,ensure_ascii=False,indent=4)
    
    
def interface():
    #interface
    print('新增排課選項系統\n\n請輸入您欲排課之系所名稱，格式如 藥學系2年級 或大學部共同整合課程4年級 (年級須為數字)')
    dep=input()
    print('請輸入欲排課程之名稱')
    classname=input()
    print('查詢中...')
    res=crawl_class_information(dep,classname)
    if len(res)==0:
        p=input('查無資料，離開請按q，重試請按其他鍵')
        if p =='q':
            exit()
        else:
            interface()
    else:
        print('查詢結果')
        target=number_wrong_interface(res)
        write_into_json(target)
        print('新增完成。該排課選項已新增至courselist.json')
        con=input('繼續排其他課程請按任意鍵，離開系統請按q')
        if con =='q':
            exit()
        else:
            interface()

interface()
        

#90
