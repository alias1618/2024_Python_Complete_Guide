# Structural Pattern Matching
# switch statement ==
# or

name = input("Enter your name: ") #string
money = input("Enter your cash amount: ") #string
hungry = input("Are you hungry? (Y/N) ") #string

match hungry:
    case "Y":
        if int(money) >= 30:
            print(f"{name} should go eat breakfast.")
        else:
            print(f"{name} is hungry but might not have enough money to buy breakfast.")
    case "N":
        if int(money) >= 30:
            print(f"{name} has budget but doesn't want to eat breakfast.")
        else:
            print(f"{name} has no money but is not hungry...")
    case _:
        print("Please make sure that you enter either Y or N.")