"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, commission_type):
        self.name = name
        self.contract_type = contract_type
        self.commission_type = commission_type
        self.monthly_salary = 0
        self.hourly_salary = 0
        self.hours = 0
        self.fixed_bonus = 0
        self.num_contracts = 0
        self.commission_rate = 0

    def get_pay(self):
        if (self.contract_type == 'monthly' and self.commission_type == 'none'):
            return self.monthly_salary
        elif (self.contract_type == 'hourly' and self.commission_type == 'none'):
            return (self.hourly_salary * self.hours)
        elif (self.contract_type == 'monthly' and self.commission_type == 'fixed'):
            return (self.monthly_salary + self.fixed_bonus)
        elif (self.contract_type == 'hourly' and self.commission_type == 'fixed'):
            return ((self.hourly_salary * self.hours) + self.fixed_bonus)
        elif (self.contract_type == 'monthly' and self.commission_type == 'variable'):
            return (self.monthly_salary + (self.num_contracts * self.commission_rate))
        elif (self.contract_type == 'hourly' and self.commission_type == 'variable'):
            return ((self.hourly_salary * self.hours) + (self.num_contracts * self.commission_rate))





    def __str__(self):
        if (self.contract_type == 'monthly' and self.commission_type == 'none'):
            return (f'{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}.')
        elif (self.contract_type == 'hourly' and self.commission_type == 'none'):
            return (f'{self.name} works on a contract of {self.hours} hours at {self.hourly_salary}/hour.  Their total pay is {self.get_pay()}.')
        elif (self.contract_type == 'monthly' and self.commission_type == 'fixed'):
            return (f'{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.fixed_bonus}.  Their total pay is {self.get_pay()}.')
        elif (self.contract_type == 'hourly' and self.commission_type == 'fixed'):
            return (f'{self.name} works on a contract of {self.hours} hours at {self.hourly_salary}/hour and receives a bonus commission of {self.fixed_bonus}.  Their total pay is {self.get_pay()}.')
        elif (self.contract_type == 'monthly' and self.commission_type == 'variable'):
            return (f'{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract.  Their total pay is {self.get_pay()}.')
        elif (self.contract_type == 'hourly' and self.commission_type == 'variable'):
            return (f'{self.name} works on a contract of {self.hours} hours at {self.hourly_salary}/hour and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract.  Their total pay is {self.get_pay()}.')


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly', 'none')
billie.monthly_salary = 4000

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', 'none')
charlie.hourly_salary = 25
charlie.hours = 100

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly', 'variable')
renee.monthly_salary = 3000
renee.num_contracts = 4
renee.commission_rate = 200

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', 'variable')
jan.hourly_salary = 25
jan.hours = 150
jan.num_contracts = 3
jan.commission_rate = 220

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', 'fixed')
robbie.monthly_salary = 2000
robbie.fixed_bonus = 1500

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', 'fixed')
ariel.hourly_salary = 30
ariel.hours = 120
ariel.fixed_bonus = 600
