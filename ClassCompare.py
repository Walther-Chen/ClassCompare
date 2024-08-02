# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:10:21 2024

@author: Tristan
"""

import openpyxl
import os
import task_kbmodified as task

data= r'C:\\Users\\Tristan\\OneDrive\\桌面\\code\\Python\\ClassCompare'
os.chdir(data)
afile= openpyxl.load_workbook('a.xlsx')
asheet=afile.worksheets[0]
astor=task.task(asheet)

#b

bfile=openpyxl.load_workbook('b.xlsx')
bsheet=bfile.worksheets[0]
bstor=task.task(bsheet)

#攤開老師
astor=task.teachers(astor)
bstor=task.teachers(bstor)



#檢查是否撞課
for i in astor:
    if i in bstor:
        if None not in i:
            print(i)
            
#ChineseYi
wb = openpyxl.Workbook()
wb.create_sheet('中乙',0)
s1= wb['中乙']
count=2
s1.cell(1,1).value='日期'
s1.cell(1,2).value='星期'
s1.cell(1,3).value='上/下午'
s1.cell(1,4).value='時間'
s1.cell(1,5).value='老師'
for j in astor:
    if j[1]=='一)'and j[2]=='P':
        if j[3]=='3-4' or j[3]=='4-5' or j[3]=='3-5':
            s1.cell(count,1).value=j[0]
            s1.cell(count,2).value=j[1]
            s1.cell(count,3).value=j[2]
            s1.cell(count,4).value=j[3]
            s1.cell(count,5).value=j[4]
            count=count+1

wb.save('chineseyi.xlsx')
