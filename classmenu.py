import classutility as util # Import the utility module
import json # Import the json module
import classtask as task # Import the task module
import classcompare as comp # Import the compare module

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
        selected_teacher = teacher_list[int(choice) - 1]
        print(f"Classes for {selected_teacher}:")
        for index, subject in enumerate(loaded_teachers[selected_teacher], start=1):
            print(f"{index}. {subject}")
        choice = input("請選擇你要排課的科目: ")
        selected_subject = loaded_teachers[selected_teacher][int(choice) - 1]
        # Display the selected teacher and subject
        print(f"授課教師: {selected_teacher}")
        print(f"授課內容: {selected_subject}")
        # Ask if the user wants to continue or exit
        choice = input("修改請按 0, 離開請按其他鍵: ")
        if choice.lower() != '0':
            return selected_subject, selected_teacher
        
def main_menu():
    print("Welcome to the Chineseyi Class Arrangement Program!")
    print("Please select an option:")
    print("1. Level 1 Classes")
    print("2. Level 2 Classes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        level1_menu()
    elif choice == "2":
        level2_menu()
    elif choice == "3":
        print("Exiting the program...")
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def level1_menu():
    print("Level 1 Classes:")
    print("1. Beginner Class")
    print("2. Intermediate Class")
    print("3. Advanced Class")
    print("4. Go back to main menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        arrange_class("Beginner Class")
    elif choice == "2":
        arrange_class("Intermediate Class")
    elif choice == "3":
        arrange_class("Advanced Class")
    elif choice == "4":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        level1_menu()

def level2_menu():
    print("Level 2 Classes:")
    print("1. Conversational Class")
    print("2. Business Class")
    print("3. Go back to main menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        arrange_class("Conversational Class")
    elif choice == "2":
        arrange_class("Business Class")
    elif choice == "3":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        level2_menu()

def arrange_class(class_name):
    print(f"Arranging class for {class_name}...")

# Start the program
#teacher_menu("teachers.json")
print(comp.yidict("a.xlsx", "b.xlsx"))