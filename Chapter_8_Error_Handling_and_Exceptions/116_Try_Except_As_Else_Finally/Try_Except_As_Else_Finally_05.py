def ask_for_int():
    while True:
        try:
            result = int(input("Enter a number here: "))
        except:
            print("Invalid number. Please try again.")
        else:
            print("Good job!")
            return result

ask_for_int()