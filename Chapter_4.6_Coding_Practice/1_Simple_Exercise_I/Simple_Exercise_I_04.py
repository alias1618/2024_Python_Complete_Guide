# 4.Write a function called "findSmallCount" that takes one list of integers and one integer as input, and returns an integer indicating how many elements in the list is smaller than the input integer.


# output
    # findSmallCount([1, 2, 3], 2); # returns 1
    # findSmallCount([1, 2, 3, 4, 5], 0); # returns 0

def findSmallCount(list1, input1):
    number = 0
    for i in list1:
        if i < input1 :
            number += 1
    
    print(number)




findSmallCount([1, 2, 3], 2)
findSmallCount([1, 2, 3, 4, 5], 0)