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
        if row1[index - 1] == ' ':
            row1[index - 1] = getCurrentSymbol()
            return True
        else:
            return False
    elif index in range(4, 7):
        if row2[index % 3 - 1] == ' ':
            row2[index % 3 - 1] = getCurrentSymbol()
            return True
        else:
            return False
    else:
        if row3[index % 3 - 1] == ' ':
            row3[index % 3 - 1] = getCurrentSymbol()
            return True
        else:
            return False

def check_winning():
    player_1_wins = False
    player_2_wins = False
    if (row1[0] == row1[1] and row1[1] == row1[2] and (" " not in row1)):
        if (row1[0] == "X"):
            player_2_wins = True
        else:
            player_1_wins = True
    elif (row2[0] == row2[1] and row2[1] == row2[2] and (" " not in row2)):
        if (row2[0] == "X"):
            player_2_wins = True
        elif (row2[0] == "O"):
            player_1_wins = True
    elif (row3[0] == row3[1] and row3[1] == row3[2] and (" " not in row3)):
        if (row3[0] == "X"):
            player_2_wins = True
        elif (row3[0] == "O"):
            player_1_wins = True
    elif (row1[0] == row2[0] and row2[0] == row3[0] and (row1[0] != " " and row2[0] != " " and row3[0] != " ")):
        if (row1[0] == "X"):
            player_2_wins = True
        elif (row1[0] == "O"):
            player_1_wins = True
    elif (row1[1] == row2[1] and row2[1] == row3[1] and (row1[1] != " " and row2[1] != " " and row3[1] != " ")):
        if (row1[1] == "X"):
            player_2_wins = True
        elif (row1[1] == "O"):
            player_1_wins = True
    elif (row1[2] == row2[2] and row2[2] == row3[2] and (row1[2] != " " and row2[2] != " " and row3[2] != " ")):
        if (row1[2] == "X"):
            player_2_wins = True
        elif (row1[2] == "O"):
            player_1_wins = True
    elif (row1[0] == row2[1] and row2[1] == row3[2] and (row1[0] != " " and row2[2] != " " and row3[2] != " ")):
        if (row1[0] == "X"):
            player_2_wins = True
        elif (row1[0] == "O"):
            player_1_wins = True
    elif (row1[2] == row2[1] and row2[1] == row3[0] and (row1[2] != " " and row2[1] != " " and row3[0] != " ")):
        if (row1[2] == "X"):
            player_2_wins = True
        elif (row1[2] == "O"):
            player_1_wins = True
    
    if player_1_wins:
        return "player 1 wins"
    elif player_2_wins:
        return "player 2 wins"
    else:
        return " no one wins" 
    

def start_game():
    while True:
        display(row1, row2, row3)
        while True:
            choice = user_choice()
            if update_table(choice):
                break
            else:
                print("Wrong position to put your choice")
        result = check_winning()
        if result == "player 1 wins":
            display(row1, row2, row3)
            print("Player 1 wins!! Congrats")
            return
        elif result == "player 1 wins":
            display(row1, row2, row3)
            print("Player 1 wins!! Congrats")
            return
        elif result == "player 2 wins":
            display(row1, row2, row3)
            print("Tie game!!")
            return

start_game()