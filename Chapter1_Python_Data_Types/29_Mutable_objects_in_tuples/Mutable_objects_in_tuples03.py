a = ([1,2,3], "Wilson") #dictionary key? Nope!
a[0][1] = 100
print(a)

# if an element in a tuple is mutable, then we can just
# select the element, and then change it.

# if we want to use a tuple as a dictionary key,
# then all elements in the tuple has to be immutable

# 15                                        #dictionary key? Yes
# 'Bob'                                     #dictionary key? Yes
# ('Tom', [14, 23, 27])                     #dictionary key? Nope
# ['filename', (15, 16)]  List is mutable   #dictionary key? Nope
# "filename"                                #dictionary key? Yes
# ("filname", 25, "extension")              #dictionary key? Yes