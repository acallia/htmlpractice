#id,manufacturer,model,displ,year,cyl,trans,drv,cty,hwy,fl,class
#1,audi,a4,1.8,1999,4,auto(l5),f,18,29,p,compact
#2,audi,a4,1.8,1999,4,manual(m5),f,21,29,p,compact
#3,audi,a4,2,2008,4,manual(m6),f,20,31,p,compact

import csv
student_name = "Amanda Callia"

with open('mpg.csv') as file:
    mpg_reader = csv.reader(file)
    next (mpg_reader) #skipping first line
    num_vehicles = 0
    sum_city = 0
    num_city = 0
    sum_hwy = 0
    num_suv = 0
    sum_suv = 0
    num_ford = 0
    sum_ford = 0
    for row in mpg_reader:
        num_vehicles += 1
        sum_city += int(row[8])
        sum_hwy += int(row[9])

        if row[1] == 'city':
            num_city += 1
            sum_city += int(row[9])

        if row[1] == 'hwy':
            num_hwy += 1
            sum_hwy += int(row[9])

        if row[1] == 'ford':
            num_ford += 1
            sum_ford += int(row[9])

        if row[11] == 'suv':
            num_suv += 1
            sum_suv += int(row[8])


avg_city = sum_city / num_vehicles
avg_hwy = sum_hwy / num_vehicles
ford_hwy = sum_ford / num_ford
suv_city = sum_suv / num_suv

with open("acalli4_assignment4.txt", "w") as output:
    output.write("avg_cty = %.2f\navg_hwy = %.2f\nford_hwy = %.2f\nsuv_city = %.2f"%(avg_city,avg_hwy,ford_hwy,suv_city))

    #output.write("The avg city mileage for all vehicles is " + str(avg_city))
    #output.write("The avg highway mileage for all vehicles is " + str(avg_hwy))
    #output.write("The avg highway mileage for all Ford vehicles is " + str(ford_hwy))
    #output.write("The avg city mileage for all SUV vehicles is" + str(suv_city))

file.close()


#print("The avg mpg for city is " + str(avg_city))



#print("The city for all is " + str(avg_city))
