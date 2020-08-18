import sqlalchemy as db
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta

student_name = "Amanda Callia"

def main():
  engine = db.create_engine('sqlite:///customer.sqlite')
  connection = engine.connect()
  results = connection.execute("select * from customer")

  with open("acalli4_assignment5.csv", "w") as file:
     cust_write = csv.writer(file)
     cust_write.writerow(["Customer ID", "Name", "Age"])
     for row in results:
         cust_write.writerow([ (row[0]), full_name(row[1], row[2]), age(row[3]) ])







def full_name(f,l):
    return f + " " + l

def age(d):
    dob = datetime.strptime(d, '%Y-%m-%d')
    today = datetime.today()
    age = relativedelta(today, dob)
    return age.years

    connection.close()


main()
