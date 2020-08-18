import glob
# import csv

py_files = glob.glob('*_assignment4.py')
if not py_files:
    print('No assignment 4 files found. Confirm the file is present and named correctly')

for py_file in py_files:
    grade = 5
    num_for_loops = 0
    open_csv = True
    open_txt = True
    paws_id = py_file.replace('_assignment4.py', '')
    with open(py_file) as file:
        for line in file:
            if ('open' in line) and ('mpg.csv' in line):
                open_csv = True
                if 'with' in line:
                    open_csv = False
            # if open_csv and ('close' in line):


            if ('open' in line) and ('txt' in line):
                open_txt = True
                if 'with' in line:
                    open_txt = False

            if 'close()' in line:
                print(line)
                open_csv = False
                open_txt = False

            if line.strip().startswith('for '):
                num_for_loops += 1
                print(line)

        if num_for_loops > 1:
            print("Too many 'for loops': " + py_file)
            grade -= ((num_for_loops - 1) * 10)

        if open_csv:
            print("CSV file was not closed")
            grade -= 10

        if open_txt:
            print("TXT file as not closed")
            grade -= 10

    try:
        py_file = py_file.replace('.py', '')
        a4 = __import__(py_file)
        if a4.student_name:
            grade += 5
        else:
            print("Variable student_name does not exist")

        txt_file = glob.glob(paws_id+'_assignment4.txt')
        if txt_file:
            grade += 20
        else:
            print("Output file " + paws_id+'_assignment4.txt' + 'does not exist')

        if round(a4.avg_city, 2) == 16.86:
            grade += 15
        else:
            print("Your avg_city is not correct.")

        if round(a4.avg_hwy, 2) == 23.44:
            grade += 15
        else:
            print("Your avg_hwy is not correct.")

        if a4.ford_hwy== 19.36:
            grade += 20
        else:
            print("Your ford_hwy is not correct.")

        if a4.suv_city == 13.5:
            grade += 20
        else:
            print("Your suv_city is not correct.")

        print("The grade for " + a4.student_name + " should be: " + str(grade))
        if grade >= 90:
            print("Another 'A'! Keep up the good work.")
    except:
        print("There appears to be syntax errors in your code.")
