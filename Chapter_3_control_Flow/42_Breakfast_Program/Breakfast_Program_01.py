# program asks user's name
# cash
# Y/N
# program checks if the user has more than or equal to $30

name = input("Enter your name: ") #string
money = input("Enter your cash amount: ") #string
hungry = input("Are you hungry? (Y/N) ") #string

if hungry == "Y":
    if int(money) >= 30:
        print(f"{name} should go eat breakfast.")
    else:
        print(f"{name} is hungry but might not have enough money to buy breakfast.")
elif hungry == "N":
    if int(money) >= 30:
        print(f"{name} has budget but doesn't want to eat breakfast.")
    else:
        print(f"{name} has no money but is not hungry...")
else:
    print("Please make sure that you enter either Y or N.")