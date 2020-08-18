from datetime import datetime
from dateutil.relativedelta import relativedelta

class Customer:

    student_name = "Amanda Callia"

    def __init__(self, id, f_name, l_name, dob, city, state, zip):
        self.id = id
        self.first_name = f_name
        self.last_name = l_name
        self.dob = dob
        self.city = city
        self.state = state
        self.zip = zip

    def full_name(self):
        return self.first_name + " " + self.last_name


    def age(self):
        dob = datetime.strptime(self.dob, '%Y-%m-%d')
        today = datetime.today()
        age = relativedelta(today, dob)
        return age.years

    def adult(self):
        return self.age() >= 18 #boolean statement

    def to_json(self):
        d = {}
        d['adult'] = self.adult()
        d['first_name'] = self.first_name
        d['last_name'] = self.last_name
        d['dob'] = self.dob
        d['city'] = self.city
        d['state'] = self.state
        d['zip'] = self.zip

        return d
