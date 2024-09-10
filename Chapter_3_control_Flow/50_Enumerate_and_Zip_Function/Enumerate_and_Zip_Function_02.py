for counter, char in enumerate("How are you today?"):
    if counter < 10:
        print(char)



#   不使用enumerate變成要這樣寫
#   都是輸出相同結果

# counter = 0
# for letter in "How are you today?":
#     if counter < 10:
#         print(letter)
#     counter += 1