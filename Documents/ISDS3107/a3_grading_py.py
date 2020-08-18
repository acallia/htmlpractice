import glob
# import csv

emp_numbers = [123, 124, 128, 125, 126, 127]
emp_numbers.sort()
emp_names = ['Bob', 'Susan', 'Abby', 'Henry', 'Edward', 'James']
emp_names.sort()

py_files = glob.glob('*_assignment3.py')
if not py_files:
    print('No assignment 3 files found. Confirm the file is present and named correctly')

for py_file in py_files:
    grade = 5
    num_for_loops = 0
    with open(py_file) as file:
        for line in file:
            if line.startswith('for') and ('mpg' in line):
                num_for_loops += 1
                print(line)
            if line.startswith('for') and ('employees' in line):
                num_for_loops += 1
                print(line)
        if num_for_loops < 2:
            print("Not using for loops: " + py_file)
    try:
        py_file = py_file.replace('.py', '')
        a3 = __import__(py_file)
        if a3.student_name == "Your name":
            print("You did not change student_name to your name")
        else:
            grade += 5

        if a3.num_items == 34:
            grade += 10
        else:
            print("Your num_items is not correct.")

        if a3.sum_items == 549:
            grade += 15
        else:
            print("Your sum_items is not correct.")

        if round(a3.avg_num, 2) == 16.15:
            grade += 15
        else:
            print("Your avg_num is not correct.")

        if a3.largest_num == 22:
            grade += 15
        else:
            print("Your largest_num is not correct.")

        if a3.smallest_num == 11:
            grade += 15
        else:
            print("Your smallest_num is not correct.")

        a3.emp_numbers.sort()
        if a3.emp_numbers == emp_numbers:
            grade += 10
        else:
            print("Your emp_numbers list is not correct.")

        a3.emp_names.sort()
        if a3.emp_names == emp_names:
            grade += 10
        else:
            print("Your emp_names list is not correct.")

        print("The grade for " + a3.student_name + " should be: " + str(grade))
        if grade >= 90:
            print("Another 'A'! Keep up the good work.")
    except:
        print("There appears to be syntax errors in your code.")
