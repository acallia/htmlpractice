# Note: you must use python for loops for this assignment.
student_name = "Amanda Callia"

# List of vehicle milage
mpg = [18,21,20,21,16,18,18,18,16,20,19,15,17,17,15,15,17,16,14,11,14,13,12,16,15,16,15,15,14,11,11,14,19,22]

num_items = 0
sum_items = 0
avg_num = 0
smallest_num = mpg[19]
largest_num = mpg[33]

# Write your for loop and conditional logic here:
sum_items = 0
for num_items in mpg.int():
    sum_items = sum_items +num_items

avg_num  = sum_items / len(mpg)







# Output the results
print("The number of items: ", num_items)
print("The sum of the items: ", sum_items)
print("The average of the items: ", avg_num)
print("The smallest number :", smallest_num)
print("The largest number :", largest_num)



# Dictiory of employees
employees = {123: 'Bob', 124: 'Susan', 128: 'Abby', 125: 'Henry', 126: 'Edward', 127: 'James'}

emp_numbers = []
emp_names = []

# Write your for loop here:
for emp_numbers, emp_names in employees.items():

# Output the results
    print("List of employee numbers: ", emp_numbers)
    print("List of employee names: ", emp_names)
