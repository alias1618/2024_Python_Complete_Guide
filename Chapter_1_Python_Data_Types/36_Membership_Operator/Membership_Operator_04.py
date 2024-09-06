myString = "Today is a good day. The weather in Hawaii is not bad."

isIn = False
for i in range(len(myString)):
    if "A" == myString[i]:
        isIn = True
print(isIn)