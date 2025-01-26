row1 = [' ',' ',' ',]
row2 = [' ',' ',' ',]
row3 = [' ',' ',' ',]

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

def user_choice():
    choice = input("Please enter a number (1-9): ")
    while not choice.isdigit() or (int(choice) not in range(1, 10)):
        if not choice.isdigit():
            print("Sorry, your choice is not valid")
        else:
            print("Your choice is not within the range of 1 - 9.")
        choice = input("Please enter a number (1-9): ")
    return int(choice)

user_choice()