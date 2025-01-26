class Employee:
    def __init__(self):
        self.income = 0


    def earn_money(self, money):
        self.income += money


    @property
    def tax_amount(self):
        return self.income * 0.05
    
    @tax_amount.setter
    def tax_amount(self, tax_number):
        self.income = tax_number * 20
    
    
wilson = Employee()

wilson.tax_amount = 200
print(wilson.income)