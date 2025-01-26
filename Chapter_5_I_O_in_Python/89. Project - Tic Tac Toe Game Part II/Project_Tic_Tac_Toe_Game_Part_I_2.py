counter = 0
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


# 1 user input 0
# 2 user input X
# 3 user input 0

def getCurrentSymbol():
    global counter
    symbol_list = ['X', 'O']
    counter += 1
    return symbol_list[counter % 2]


def update_table(index):
    if index in range(1, 4):
        row1[index - 1] = getCurrentSymbol()
    elif index in range(4, 7):
        row2[index % 3 - 1] = getCurrentSymbol()
    else:
        row3[index % 3 - 1] = getCurrentSymbol()


def start_game():
    while True:
        display(row1, row2, row3)
        choice = user_choice()
        update_table(choice)