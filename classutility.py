"""
    class_utility.py
    排課程式需要的額外工具模組
"""
import json # 載入 json 模組
import classtask as task # 載入 class_task 模組

def print_table(data):
    """
        Print a table of data with columns of equal width, separated by a line of dashes, left-aligned and padded with spaces, with word wrap
    """
    # Find the maximum width of each column
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
    # Print the header row
    print_separator(column_widths)
    print_row(data[0], column_widths)
    print_separator(column_widths)
    # Print the data rows
    for row in data[1:]:
        print_row(row, column_widths)
    print_separator(column_widths)
    
def print_row(row, column_widths):
    # Print each cell in the row with the appropriate width
    for item, width in zip(row, column_widths):
        print(f"{str(item):<{width}}", end="  ")
    print()

def print_separator(column_widths):
    # Print a separator line between the header and the rows
    for width in column_widths:
        print("-" * width, end="  ")
    print()

# Example usage
data = [
    [u"授課時間", u"授課老師", u"主題", u"備註"],
    ["2021-09-01", "John Doe", "Python Basics", "與醫學系上課時間重疊"],
    ["2021-09-08", "John Doe", "Python Functions", "假日"],
    ["2021-09-15", "John Doe", "Python Modules", "第三堂課"]
]

print_table(data)
def table_expand(data):
    """
        Expand a list of dates into a table with columns for date, teacher, subject, and notes
    """
    expanded_table = []
    expanded_table.append(["授課日期", "授課時間", "授課老師", "主題", "備註"])
    for date in data:
        # Split the date into year, month, and day
        year, month, day = date.split("/")
        # Create a new row for each class
        expanded_table.append([f"{year}/{month}/{day}", "", "", "", ""])
    return expanded_table

def load_teachers(filename):
    """
        load teachers and their classes from a JSON file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            teachers = json.load(file)
            return teachers
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    
def save_teachers(filename, teachers):
    """
        save teachers and their classes to a JSON file
    """
    with open (filename, 'w', encoding='utf-8') as file:
        json.dump(teachers, file, ensure_ascii=False, indent=4)

# Write a sample JSON file for teachers and classes
teachers = {
    "John Doe": ["Python Basics", "Python Functions", "Python Modules"],
    "Jane Smith": ["Web Development", "Database Management"]
}
save_teachers("teachers.json", teachers)

# Load the teachers and classes from the JSON file
loaded_teachers = load_teachers("teachers.json")
print(loaded_teachers)      



print_table(table_expand(task.ChineseYiDate()))