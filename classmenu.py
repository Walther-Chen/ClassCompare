"""
    classmenu.py
    排課程式的CLI介面
    KB 2024/08/11 @ CMU
"""

import classutility as util # Import the utility module
import json # Import the json module
import classtask as task # Import the task module
import ClassCompare as comp # Import the compare module
import openpyxl
import os

def teacher_menu (filename):
    """
        A two level CLI menu for teachers and their classes, using multiple choice selection to select teacher and subject
    """
    loaded_teachers = util.load_teachers(filename)
    while True:
        # Create a list of keys in the loaded_teachers dictionary first, and display them with index numbers
        teacher_list = list(loaded_teachers.keys())
        print("Teachers:")
        for index, teacher in enumerate(teacher_list, start=1):
            print(f"{index}. {teacher}")
        choice = input("請選擇你要排課的老師: ")
        #list the classes of the selected teacher, and display them with index numbers
        try:
            selected_teacher = teacher_list[int(choice) - 1]
        except IndexError:
            print("Invalid choice. Please try again.")
            continue
        print(f"Classes for {selected_teacher}:")
        for index, subject in enumerate(loaded_teachers[selected_teacher], start=1):
            print(f"{index}. {subject}")
        choice = input("請選擇你要排課的科目: ")
        try: 
            selected_subject = loaded_teachers[selected_teacher][int(choice) - 1]
        except IndexError:
            print("Invalid choice. Please try again.")
            continue
        # Display the selected teacher and subject
        print(f"授課教師: {selected_teacher}")
        print(f"授課內容: {selected_subject}")
        # Ask if the user wants to continue or exit
        choice = input("修改請按 0, 離開請按其他鍵: ")
        if choice.lower() != '0':
            return selected_subject, selected_teacher
        
def main_menu(classchart):
    print("中乙排課系統")
    print("目前課表：")
    util.print_chungyi(classchart)
    choice = input("請用序號選擇你要排哪一堂課，輸入q離開並存檔")

    if choice == "q":
        print("Exiting the program...")
        # Save the classchart to a excel file, do not use content manager
        wb = openpyxl.Workbook()
        ws = wb.active
        for row in classchart:
            ws.append(row)
        wb.save("classchart.xlsx")
        print("課表已經存到 classchart.xlsx")
        return

    elif choice.isdigit():
        choice = int(choice)
        if choice > 0 and choice < len(classchart):            
            classchart[choice][3], classchart[choice][2] = teacher_menu("teachers.json")            
            main_menu(classchart)
        else:
            print("Invalid choice. Please try again.")
            main_menu(classchart)


# Start the program
r=os.path.dirname(__file__)
os.chdir(r)
classchart = comp.yilist_generation("a.xlsx", "b.xlsx")
#print(classchart)
main_menu(classchart)

