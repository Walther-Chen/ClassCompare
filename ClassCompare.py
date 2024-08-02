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
            

       
