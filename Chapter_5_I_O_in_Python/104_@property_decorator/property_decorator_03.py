class Employee:
    def __init__(self):
        self.income = 0


    def earn_money(self, money):
        self.income += money


    @property
    def tax_amount(self):
        return self.income * 0.05
    
    
wilson = Employee()
wilson.earn_money(300)
print(wilson.tax_amount)    # tax_amount is not a real property
#   tax_mount virtual property is read-only