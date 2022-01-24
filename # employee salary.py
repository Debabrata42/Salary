# employee salary
class Employee:
    def __init__(self, basic_salary = 500):
     self.basic_salary = basic_salary

class Chef(Employee):
    def __init__(self,hourly_wage,hours,days):
     super().__init__()
     self.hourly_wage = hourly_wage
     self.hours = hours
     self.days = days

    def get_monthly_income(self):
      return self.hourly_wage * self.hours * self.days + self.basic_salary

class Waiter(Employee):
    def __init__(self,hourly_wage,hours,days):
      super().__init__()
      self.hourly_wage = hourly_wage
      self.hours = hours
      self.days = days
      tips = int(input("Enter the tips:"))
    def get_monthly_income(self):
      return self.hourly_wage * self.hours * self.days + self.basic_salary
class Cleaner(Employee):
    def __init__(self,monthly_salary,extra_hours,extra_hour_wage):
      super().__init__()
      self.monthly_salary = monthly_salary
      self.extra_hours = extra_hours
      self.extra_hour_wage = extra_hour_wage
    def get_monthly_income(self):
      return self.monthly_salary + self.extra_hours* self.extra_hour_wage\
             + self.basic_salary

NumberofChef = int(input("Enter how many Chef: "))
WorkingHour = int(input("Working Hour: "))
WorkingDay = int(input("Working Day: "))
Rahim = Chef(NumberofChef,WorkingHour,WorkingDay)

Rahim_salary = Rahim.get_monthly_income()
print("salary of Chef: ",Rahim_salary,"Taka")

NumberofWaiter = int(input("Enter how many Waiter: "))
WorkingHour = int(input("Working Hour: "))
WorkingDay = int(input("Working Day: "))
Sumon = Waiter(NumberofWaiter,WorkingHour,WorkingDay)

Sumon_salary = Sumon.get_monthly_income()
print("Salary of Waiter",Sumon_salary,"Taka")

NumberofCleaner = int(input("Enter how many Cleaner: "))
WorkingHour = int(input("Working Hour: "))
WorkingDay = int(input("Working Day: "))
Karim = Cleaner(NumberofCleaner,WorkingHour,WorkingDay)

Karim_salary = Karim.get_monthly_income()
print("salary of Cleaner: ",Karim_salary,"Taka")

TotalIncome = int(input("How many income: "))
#income = 20000
profit = TotalIncome - Rahim_salary - Sumon_salary - Karim_salary
print("Total profit: ",profit,"Taka")
 