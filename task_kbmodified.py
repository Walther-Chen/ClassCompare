# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:35:52 2024

@author: Tristan
"""
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

def ChineseYi (class_sort):
    print(1)